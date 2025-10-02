# 🛒 Ecommerce Fake Dashboard

Projeto simples em **Python + Streamlit** que consome a [Fake Store API](https://fakestoreapi.com/), salva os resultados em CSV e exibe um dashboard interativo.

---

## 📂 Estrutura do projeto

- 🗂️ **ecommerce-fake/** (pasta raiz do projeto)  
  - 📁 **data/** → onde vão ficar os CSVs gerados  
  - 📁 **src/** → código-fonte do projeto  
    - 📁 **api/**  
      - 📄 `product_search.py` → script que consulta a Fake Store API e salva CSV  
    - 📁 **app/**  
      - 📄 `app.py` → dashboard em Streamlit  
  - 📄 **requirements.txt** → lista de dependências do projeto  
  - 📄 **.env** → variáveis de ambiente (API URL, câmbio, checkout URL)  
  - 📄 **README.md** → documentação do projeto  
  - ⚠️ **.venv/** → ambiente virtual (não criar manualmente, será gerado pelo comando `python -m venv .venv`)  

---

## ✅ Tecnologias usadas

- 🐍 Python  
- 📊 Pandas  
- 🌐 Requests  
- 🔑 python-dotenv  
- 🎨 Streamlit  

---

## ⚙️ Setup do projeto (Streamlit Cloud)

Este projeto está publicado no **Streamlit Cloud**, então você não precisa instalar nada localmente.  
Basta acessar o link abaixo e usar direto no navegador (funciona em desktop 💻 e mobile 📱):

👉 [Abrir o Dashboard no Streamlit Cloud](https://streamlit.io/cloud) <!-- substitua pelo link real do seu app -->

---

### 🔑 Variáveis de ambiente

No Streamlit Cloud, as variáveis do arquivo `.env` devem ser configuradas em:

**Settings → Secrets**  

Exemplo de configuração:

```toml
FAKESTORE_API_URL="https://fakestoreapi.com/products"
USD_TO_BRL="5.5"
STRIPE_CHECKOUT_URL="https://checkout.stripe.com/test"
