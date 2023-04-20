import streamlit as st
import pandas as pd
from PIL import Image

# Integrante do trabalho
# Arthur Vinicius Santos Silva RA:1903665
# Carolina Gabrielle Castro Vieira RA:1900127

# Criando dataframe a partir dos dados extraídos na AC2
df = pd.read_csv("1_bases_tratadas/base_tratada.csv")
df["preco_original"] = df["preco"] / (1 - (df["porcentagem_desconto"]/100))
df["preco_original"] = round(df["preco_original"], 2)
# -------------------------------------------------------

# Título da página
col1, col2, col3 = st.columns(3)
st.markdown(
    f"""
    <div style='text-align: center;'>
        <h1>Loja Nuuvem</h1>
    </div>
    """,
    unsafe_allow_html=True
)
with col2:
  image = Image.open('assets/nuuvem.png')
  st.image(image, caption='Logo Loja Nuuvem')

st.divider() 
# -------------------------------------------------------


# Gráfico com line chart do preço dos jogos
st.subheader('Variação do preço dos jogos')
st.line_chart(df.preco)
st.caption(f'Quantidade de itens: {len(df)}')
st.divider() 
# -------------------------------------------------------


# Filtra jogos pelo nome
st.subheader('Encontre o jogo pelo nome')
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

text_input = st.text_input(
    "Nome do jogo buscado 👇",
    label_visibility=st.session_state.visibility,
    disabled=st.session_state.disabled,
    placeholder="Digite o nome do jogo",
)

if text_input:
    df_filtrado = df[df["nome"].str.contains(text_input, case=False)]
    df_filtrado = df_filtrado.rename(columns={
    "nome": "Nome do Jogo",
    "porcentagem_desconto": "Desconto (%)",
    "preco": "Preço (R$)",
    "tipo": "Tipo de Jogo",
    "preco_original": "Preço original(R$)"
    })
    st.dataframe(df_filtrado[["Nome do Jogo", "Preço original(R$)", "Preço (R$)", "Desconto (%)"]], use_container_width=True)
    if len(df_filtrado) == 0:
      st.info('Jogo não encontrado!', icon="ℹ️")
st.divider() 
# -------------------------------------------------------


# Filtro para listar jogos pelo preço
st.subheader('Encontre os jogos pela faixa de preço')
max = int(df['preco'].max()) + 1 
valor_jogo_min = st.slider('Mínimo BRL$', 0, max, 5)
valor_jogo_max = st.slider('Máximo BRL$', 0, max, 100)
if valor_jogo_min > valor_jogo_max:
  st.error('O valor mínimo, não pode ser maior que o máximo.', icon="🚨")
valores_filtrados_preco = df.loc[df['preco'].between(valor_jogo_min, valor_jogo_max)].sort_values(by=['porcentagem_desconto'], ascending=False)
valores_filtrados_preco = valores_filtrados_preco.rename(columns={
    "nome": "Nome do Jogo",
    "porcentagem_desconto": "Desconto (%)",
    "preco": "Preço (R$)",
    "tipo": "Tipo de Jogo",
    "preco_original": "Preço original(R$)"
})
st.dataframe(valores_filtrados_preco[["Nome do Jogo", "Preço original(R$)","Preço (R$)", "Desconto (%)"]], use_container_width=True)
st.caption(f'Quantidade de itens: {len(valores_filtrados_preco)}')
st.divider() 
# -------------------------------------------------------


# TOP 10 Jogos com maior desconto 
st.subheader('TOP 10 Jogos com maior desconto')
jogos_mais_85_desconto = df.sort_values(by=['porcentagem_desconto'], ascending=False).head(10)
jogos_mais_85_desconto = jogos_mais_85_desconto.rename(columns={
    "nome": "Nome do Jogo",
    "porcentagem_desconto": "Desconto (%)",
    "preco": "Preço (R$)",
    "tipo": "Tipo de Jogo",
    "preco_original": "Preço original(R$)"
    })

st.dataframe(jogos_mais_85_desconto[["Nome do Jogo", "Preço original(R$)", "Preço (R$)", "Desconto (%)"]], use_container_width=True)
st.caption(f'Quantidade de itens: {len(jogos_mais_85_desconto)}')
st.divider() 
# -------------------------------------------------------


#-------------------------------------------------- plotly
st.subheader('Agrupamento de jogos por quantidade de desconto')













st.markdown(
   """
    <h4 style='text-align: center;'>
        Designed by
        <a href="https://github.com/thuurzz" style='text-decoration: none;'>
            @thuurrzz
        </a>
    </h4>
   """,
   unsafe_allow_html=True
)
