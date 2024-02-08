import streamlit as st
import itertools
import random

# Lista de países
PAISES = [
    "Alemanha", "Argentina", "Austrália", "Brasil", "Camarões",
    "Coreia do Sul", "Dinamarca", "Escócia", "Espanha", "Estados Unidos",
    "França", "Grécia", "Inglaterra", "República da Irlanda", "Itália",
    "México", "Nigéria", "Portugal", "Chéquia", "Suécia"
]

# Dicionário com as cores correspondentes aos países
CORES_EQUIPES = {
    pais: "#{:06x}".format(random.randint(0, 0xFFFFFF)) for pais in PAISES
}

def cadastrar_equipes():
    equipes_selecionadas = st.multiselect("Selecione as equipes:", options=PAISES, default=PAISES)
    return equipes_selecionadas

def criar_grupos(equipes):
    random.shuffle(equipes)  # Embaralha as equipes
    grupos = [f"Grupo {i}" for i in range(1, 6)]
    equipe_por_grupo = len(equipes) // len(grupos)
    grupos_equipes = [equipes[i:i + equipe_por_grupo] for i in range(0, len(equipes), equipe_por_grupo)]
    return dict(zip(grupos, grupos_equipes))

def gerar_jogos(grupos):
    jogos = []
    for grupo in grupos.values():
        jogos_grupo = list(itertools.combinations(grupo, 2))
        random.shuffle(jogos_grupo)  # Embaralha os jogos
        jogos.extend(jogos_grupo)
    return jogos

def cadastrar_placar(jogos):
    st.title("Cadastro de Placar")
    st.write("Insira o placar de cada jogo:")

    placares = []
    for idx, jogo in enumerate(jogos, start=1):
        placar = st.text_input(f"Placar do Jogo {idx} ({jogo[0]} vs {jogo[1]}):", key=f"placar_{idx}")
        placares.append(placar)

    st.write("\nPlacares cadastrados:")
    for idx, placar in enumerate(placares, start=1):
        st.write(f"Jogo {idx}: {placar}")

def main():
    menu = ["Cadastro de Equipes e Geração de Jogos", "Cadastro de Placar"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Cadastro de Equipes e Geração de Jogos":
        st.title("Cadastro de Equipes e Geração de Jogos")
        st.write("Por favor, selecione as equipes participantes:")

        equipes_selecionadas = cadastrar_equipes()

        grupos = criar_grupos(equipes_selecionadas)

        st.write("\nGrupos Criados:")
        for nome_grupo, equipes_grupo in grupos.items():
            st.write(f"{nome_grupo}:")
            table_data = []
            for equipe in equipes_grupo:
                table_data.append([equipe])
            st.table(table_data)

        jogos = gerar_jogos(grupos)

        st.write("\nJogos Gerados:")
        table_jogos = [["Jogo", "Equipes"]]
        for idx, jogo in enumerate(jogos, start=1):
            table_jogos.append([f"Jogo {idx}", f"{jogo[0]} vs {jogo[1]}"])
        st.table(table_jogos)

    elif choice == "Cadastro de Placar":
        jogos = gerar_jogos(criar_grupos(cadastrar_equipes()))
        cadastrar_placar(jogos)

if __name__ == "__main__":
    main()
