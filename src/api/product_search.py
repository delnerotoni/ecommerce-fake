import requests
import pandas as pd
import os
from dotenv import load_dotenv
import sys

# Carregar variáveis do .env
load_dotenv()

API_URL = os.getenv("FAKESTORE_API_URL", "https://fakestoreapi.com/products")
USD_TO_BRL = float(os.getenv("USD_TO_BRL", 5.5))

# Mini dicionário de tradução PT → EN
TRANSLATIONS = {
    "camiseta": "shirt",
    "camisa": "shirt",
    "calça": "pants",
    "jaqueta": "jacket",
    "bolsa": "bag",
    "anel": "ring",
    "colar": "necklace",
    "brinco": "earring",
    "sapato": "shoes"
}

def translate_query(query: str) -> str:
    """Traduz termos em PT para EN se existir no dicionário."""
    return TRANSLATIONS.get(query.lower(), query)

def search_products(query: str):
    """Busca produtos na Fake Store API e retorna lista filtrada."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        products = response.json()
    except Exception as e:
        print(f"❌ Erro ao consultar API: {e}")
        return []

    # Filtrar produtos pelo termo (case-insensitive)
    filtered = [
        p for p in products
        if query.lower() in p["title"].lower() or query.lower() in p["description"].lower()
    ]
    return filtered

def save_to_csv(products, query: str):
    """Salva os produtos em um CSV dentro da pasta data/."""
    if not products:
        print(f"⚠️ Nenhum produto encontrado para '{query}'.")
        return

    df = pd.DataFrame(products)

    # Adicionar coluna com preço convertido
    df["price_brl"] = df["price"].apply(lambda x: round(x * USD_TO_BRL, 2))

    # Selecionar colunas mais úteis
    df = df[["id", "title", "category", "price", "price_brl", "description", "image"]]

    os.makedirs("data", exist_ok=True)
    file_path = f"data/results_{query}.csv"
    df.to_csv(file_path, index=False, encoding="utf-8")
    print(f"✅ Resultados salvos em {file_path}")

    # Preview no terminal
    print("\n📊 Pré-visualização dos primeiros produtos:")
    print(df.head(3).to_string(index=False))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python src/api/product_search.py <termo_de_busca>")
        sys.exit(1)

    query = sys.argv[1]
    translated_query = translate_query(query)

    if translated_query != query:
        print(f"🌐 Traduzindo '{query}' → '{translated_query}'")

    print(f"🔎 Buscando produtos com termo: {translated_query}")
    products = search_products(translated_query)
    save_to_csv(products, query)
