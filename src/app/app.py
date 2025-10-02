import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
import os

# Tradução automática
try:
    from deep_translator import GoogleTranslator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    TRANSLATOR_AVAILABLE = False

# Carregar variáveis do .env
load_dotenv()
API_URL = os.getenv("FAKESTORE_API_URL", "https://fakestoreapi.com/products")
USD_TO_BRL = float(os.getenv("USD_TO_BRL", 5.5))
CHECKOUT_URL = os.getenv("STRIPE_CHECKOUT_URL", "https://checkout.stripe.com/test")

st.set_page_config(page_title="Ecommerce Fake Dashboard", layout="wide")

st.title("🛒 Ecommerce Fake Dashboard")
st.markdown("Explore os produtos buscados na Fake Store API")

# Inicializar carrinho
if "cart" not in st.session_state:
    st.session_state.cart = []

# Tradução de categorias
CATEGORY_TRANSLATIONS = {
    "men's clothing": "Roupas masculinas",
    "women's clothing": "Roupas femininas",
    "jewelery": "Joias",
    "electronics": "Eletrônicos"
}

# Buscar produtos da API
@st.cache_data
def load_products():
    try:
        resp = requests.get(API_URL, timeout=10)
        resp.raise_for_status()
        products = resp.json()
        df = pd.DataFrame(products)
        df["price_brl"] = df["price"].apply(lambda x: round(x * USD_TO_BRL, 2))
        return df
    except Exception as e:
        st.error(f"❌ Erro ao carregar produtos: {e}")
        return pd.DataFrame()

df = load_products()

if df.empty:
    st.stop()

# Sidebar - filtros
st.sidebar.header("🔎 Filtros")

categories = ["Todas"] + [CATEGORY_TRANSLATIONS.get(c, c) for c in sorted(df["category"].unique())]
selected_cat = st.sidebar.selectbox("📑 Selecione a categoria", categories)

filtered_df = df.copy()
if selected_cat != "Todas":
    original_cat = [k for k, v in CATEGORY_TRANSLATIONS.items() if v == selected_cat]
    if original_cat:
        filtered_df = df[df["category"] == original_cat[0]]

# Traduzir títulos para exibir no multiselect
def translate_text(text):
    if TRANSLATOR_AVAILABLE:
        try:
            return GoogleTranslator(source="en", target="pt").translate(text)
        except Exception:
            return text
    return text

product_options = {row["id"]: translate_text(row["title"]) for _, row in filtered_df.iterrows()}
selected_products = st.sidebar.multiselect("🛍️ Selecione os produtos desejados", options=list(product_options.keys()), format_func=lambda x: product_options[x])

st.success(f"✅ {len(selected_products)} produto(s) selecionado(s)")

# Exibir produtos escolhidos
for _, row in filtered_df[filtered_df["id"].isin(selected_products)].iterrows():
    with st.container():
        cols = st.columns([1, 3])
        with cols[0]:
            st.image(row["image"], width=150)
        with cols[1]:
            title_pt = translate_text(row["title"])
            desc_pt = translate_text(row["description"])

            st.subheader(title_pt)
            cat_pt = CATEGORY_TRANSLATIONS.get(row["category"], row["category"])
            st.write(f"**Categoria:** {cat_pt}")
            st.write(f"💵 USD: ${row['price']:.2f} | 🇧🇷 BRL: R${row['price_brl']:.2f}")
            st.caption(desc_pt[:250] + "...")

            qty = st.number_input(
                f"Quantidade ({row['title'][:15]}...)", 
                min_value=1, max_value=10, value=1, step=1, key=f"qty_{row['id']}"
            )

            if st.button(f"🛒 Adicionar ao carrinho", key=f"add_{row['id']}"):
                item = row.to_dict()
                item["quantity"] = qty
                item["total_price"] = item["price"] * qty
                item["total_price_brl"] = item["price_brl"] * qty
                st.session_state.cart.append(item)
                st.success(f"{qty}x {title_pt} adicionado ao carrinho!")

    st.markdown("---")

# Sidebar - carrinho
st.sidebar.header("🛒 Carrinho")
if st.session_state.cart:
    cart_df = pd.DataFrame(st.session_state.cart)
    total_usd = cart_df["total_price"].sum()
    total_brl = cart_df["total_price_brl"].sum()

    st.sidebar.write(cart_df[["title", "quantity", "total_price", "total_price_brl"]])
    st.sidebar.markdown(f"**Total:** ${total_usd:.2f} | R${total_brl:.2f}")

    st.sidebar.markdown(f"[💳 Finalizar compra]({CHECKOUT_URL})", unsafe_allow_html=True)

    cart_csv = cart_df.to_csv(index=False).encode("utf-8")
    st.sidebar.download_button(
        label="⬇️ Baixar carrinho em CSV",
        data=cart_csv,
        file_name="carrinho.csv",
        mime="text/csv"
    )
else:
    st.sidebar.info("Carrinho vazio 🛒")

# Botão para baixar resultados filtrados
if not filtered_df.empty:
    results_csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Baixar resultados filtrados em CSV",
        data=results_csv,
        file_name="produtos_filtrados.csv",
        mime="text/csv"
    )
