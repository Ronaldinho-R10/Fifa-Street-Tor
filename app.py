import streamlit as st
import itertools
import random
import json

# Lista de países
PAISES_GRUPO_1 = ["Inglaterra", "Portugal", "Itália", "Escócia"]
PAISES_GRUPO_2 = ["Camarões", "França", "Grécia", "Nigéria"]
PAISES_GRUPO_3 = ["Alemanha", "Argentina", "República da Irlanda", "México"]
PAISES_GRUPO_4 = ["Suécia", "Brasil", "Estados Unidos", "Austrália"]
PAISES_GRUPO_5 = ["Espanha", "Coreia do Sul", "Chéquia", "Dinamarca"]

# Dicionário com as cores correspondentes aos países
CORES_EQUIPES = {
    pais: "#{:06x}".format(random.randint(0, 0xFFFFFF)) for pais in set(
        PAISES_GRUPO_1 + PAISES_GRUPO_2 + PAISES_GRUPO_3 + PAISES_GRUPO_4 + PAISES_GRUPO_5
    )
}

def cadastrar_equipes():
    st.subheader("Cadastro de Equipes")
    st.write("Grupo 1:")
    equipes_grupo_1 = [st.text_input(f"Equipe {i+1}", value=PAISES_GRUPO_1[i]) for i in range(len(PAISES_GRUPO_1))]
    st.write("Grupo 2:")
    equipes_grupo_2 = [st.text_input(f"Equipe {i+1}", value=PAISES_GRUPO_2[i]) for i in range(len(PAISES_GRUPO_2))]
    st.write("Grupo 3:")
    equipes_grupo_3 = [st.text_input(f"Equipe {i+1}", value=PAISES_GRUPO_3[i]) for i in range(len(PAISES_GRUPO_3))]
    st.write("Grupo 4:")
    equipes_grupo_4 = [st.text_input(f"Equipe {i+1}", value=PAISES_GRUPO_4[i]) for i in range(len(PAISES_GRUPO_4))]
    st.write("Grupo 5:")
    equipes_grupo_5 = [st.text_input(f"Equipe {i+1}", value=PAISES_GRUPO_5[i]) for i in range(len(PAISES_GRUPO_5))]

    return {
        "Grupo 1": equipes_grupo_1,
        "Grupo 2": equipes_grupo_2,
        "Grupo 3": equipes_grupo_3,
        "Grupo 4": equipes_grupo_4,
        "Grupo 5": equipes_grupo_5
    }

@st.cache_data(experimental_allow_widgets=True)
def main():
    st.title("Cadastro de Equipes e Geração de Jogos")
    st.write("Por favor, preencha o nome das equipes para cada grupo:")

    grupos = cadastrar_equipes()

    st.write("\nGrupos Criados:")
    for nome_grupo, equipes_grupo in grupos.items():
        st.write(f"{nome_grupo}:")
        for equipe in equipes_grupo:
            st.write(f"- {equipe}")

    # Geração de Jogos
    jogos = []
    for grupo, equipes in grupos.items():
        for jogo in itertools.combinations(equipes, 2):
            jogos.append(jogo)

    st.write("\nJogos Gerados:")
    for idx, jogo in enumerate(jogos, start=1):
        st.write(f"Jogo {idx}: {jogo[0]} vs {jogo[1]}")

    # Serialize os dados em JSON
    dados_json = {
        "Grupos": grupos,
        "Jogos": jogos
    }
    st.json(dados_json)

if __name__ == "__main__":
    main()