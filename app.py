import streamlit as st
import itertools
import random
import json

# Lista de países
PAISES_GRUPO_PADRAO = ["Portugal", "Inglaterra", "Itália", "Escócia"]
PAISES_RESTANTES = [
    "Alemanha", "Argentina", "Austrália", "Brasil", "Camarões",
    "Coreia do Sul", "Dinamarca", "Espanha", "Estados Unidos",
    "França", "Grécia", "República da Irlanda", "México",
    "Nigéria", "Chéquia", "Suécia"
]

# Dicionário com as cores correspondentes aos países
CORES_EQUIPES = {
    pais: "#{:06x}".format(random.randint(0, 0xFFFFFF)) for pais in set(
        PAISES_GRUPO_PADRAO + PAISES_RESTANTES
    )
}

def cadastrar_equipes():
    st.subheader("Cadastro de Equipes")
    st.write("Grupo Padrão:")
    equipes_grupo_padrao = [st.text_input(f"Equipe {i+1}", value=PAISES_GRUPO_PADRAO[i]) for i in range(len(PAISES_GRUPO_PADRAO))]

    st.write("Restante dos Grupos (Aleatório):")
    equipes_resto_grupos = [st.multiselect("Selecione as equipes:", options=PAISES_RESTANTES, default=random.sample(PAISES_RESTANTES, k=4)) for _ in range(4)]

    return {
        "Grupo Padrão": equipes_grupo_padrao,
        "Grupo 1": equipes_resto_grupos[0],
        "Grupo 2": equipes_resto_grupos[1],
        "Grupo 3": equipes_resto_grupos[2],
        "Grupo 4": equipes_resto_grupos[3]
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
        if grupo != "Grupo Padrão":
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
