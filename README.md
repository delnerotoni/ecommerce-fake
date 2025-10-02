# 🛒 Ecommerce Fake Dashboard

Dashboard de e‑commerce desenvolvido em **Python + Streamlit**, consumindo a **Fake Store API**.  
Permite explorar produtos, filtrar por categorias, traduzir títulos e descrições para português, adicionar itens ao carrinho, exportar resultados em CSV e simular um checkout.

⚠️ **Status:** Este projeto está em **fase de desenvolvimento e testes**. Algumas funcionalidades podem mudar ou ser ajustadas nas próximas versões.

---

## ✨ Funcionalidades

- 🔎 Busca de produtos direto da Fake Store API  
- 🗂️ Filtros por categoria (traduzidas para PT‑BR)  
- 🌐 Tradução automática de títulos e descrições (EN → PT)  
- 🛍️ Carrinho de compras com controle de quantidade  
- 💵 Totais em USD e BRL (conversão configurável)  
- 💾 Exportação em CSV (carrinho e resultados filtrados)  
- 💳 Simulação de checkout com link configurável  
- 📱 Interface responsiva (desktop e mobile)  

---

## ☁️ Acesse o app no Streamlit Cloud

Este projeto está publicado no **Streamlit Cloud**, sem necessidade de instalação local.  
Basta acessar o link abaixo e usar direto no navegador (funciona em desktop 💻 e mobile 📱):

👉 [Abrir o Dashboard no Streamlit Cloud](https://streamlit.io/cloud) <!-- substitua pelo link real do seu app -->

---

## 📂 Estrutura do projeto

- 🗂️ **src/** → código-fonte do projeto  
  - 📁 **api/** → scripts auxiliares (ex.: busca de produtos e geração de CSV)  
  - 📁 **app/** → aplicação principal em Streamlit  
- 📄 **requirements.txt** → lista de dependências  
- 📄 **.env** → variáveis de ambiente (API URL, câmbio, checkout URL)  
- 📄 **README.md** → documentação do projeto  
- ⚠️ **.venv/** → ambiente virtual (não versionado)  

---

## ✅ Tecnologias usadas

- 🐍 Python  
- 📊 Pandas  
- 🌐 Requests  
- 🔑 python-dotenv  
- 🌍 Deep Translator  
- 🎨 Streamlit  

---

## ⚙️ Setup local (opcional, para testes)

Se quiser rodar o projeto localmente em fase de testes:

```bash
git clone https://github.com/delnerotoni/ecommerce-fake.git
cd ecommerce-fake

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
