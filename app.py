import streamlit as st
import itertools

def cadastrar_equipes():
    equipes = []
    for i in range(1, 21):
        equipe = st.text_input(f"Digite o nome da equipe {i}:")
        equipes.append(equipe)
    return equipes

def criar_grupos(equipes):
    grupos = [f"Grupo {i}" for i in range(1, 6)]
    equipe_por_grupo = len(equipes) // len(grupos)
    grupos_equipes = [equipes[i:i + equipe_por_grupo] for i in range(0, len(equipes), equipe_por_grupo)]
    return dict(zip(grupos, grupos_equipes))

def gerar_jogos(grupos):
    jogos = []
    for grupo in grupos.values():
        jogos_grupo = list(itertools.combinations(grupo, 2))
        jogos.extend(jogos_grupo)
    return jogos

def main():
    st.title("Cadastro de Equipes e Geração de Jogos")
    st.write("Por favor, insira os nomes das equipes:")
    equipes = cadastrar_equipes()

    grupos = criar_grupos(equipes)

    st.write("\nGrupos Criados:")
    for nome_grupo, equipes_grupo in grupos.items():
        st.write(f"{nome_grupo}: {equipes_grupo}")

    jogos = gerar_jogos(grupos)

    st.write("\nJogos Gerados:")
    for idx, jogo in enumerate(jogos, start=1):
        st.write(f"Jogo {idx}: {jogo[0]} vs {jogo[1]}")

if __name__ == "__main__":
    main()