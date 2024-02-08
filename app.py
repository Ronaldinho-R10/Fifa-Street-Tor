import streamlit as st
import itertools

# Dicionário com as cores correspondentes aos países
CORES_EQUIPES = {
    "Alemanha": "#000000",
    "Argentina": "#75AADB",
    "Austrália": "#FFD700",
    "Brasil": "#FFD700",
    "Camarões": "#008000",
    "Coreia do Sul": "#FF0000",
    "Dinamarca": "#C60C30",
    "Escócia": "#003399",
    "Espanha": "#FF0000",
    "Estados Unidos": "#B22222",
    "França": "#0055A4",
    "Grécia": "#0D5EAF",
    "Inglaterra": "#FFFFFF",
    "República da Irlanda": "#169B62",
    "Itália": "#009246",
    "México": "#006847",
    "Nigéria": "#32CD32",
    "Portugal": "#00843D",
    "Chéquia": "#D41245",
    "Suécia": "#0065BD"
}

def cadastrar_equipes():
    equipes_selecionadas = st.multiselect("Selecione as equipes:", options=list(CORES_EQUIPES.keys()), default=list(CORES_EQUIPES.keys()))
    return equipes_selecionadas

def criar_grupos(equipes):
    grupos = [f"Grupo {i}" for i in range(1, 6)]
    equipe_por_grupo = len(equipes) // len(grupos)
    grupos_equipes = [equipes[i:i + equipe_por_grupo] for i in range(0, len(equipes), equipe_por_grupo)]
    return dict(zip(grupos, grupos_equipes))

def gerar_jogos(grupos):
    jogos = {}
    for nome_grupo, equipes_grupo in grupos.items():
        jogos_grupo = list(itertools.combinations(equipes_grupo, 2))
        jogos[nome_grupo] = jogos_grupo
    return jogos

def main():
    st.title("Cadastro de Equipes, Geração de Grupos e Jogos")

    equipes_selecionadas = cadastrar_equipes()

    grupos = criar_grupos(equipes_selecionadas)

    st.write("\nGrupos Criados:")
    for nome_grupo, equipes_grupo in grupos.items():
        st.subheader(nome_grupo)
        for equipe in equipes_grupo:
            cor_equipe = CORES_EQUIPES[equipe]
            st.markdown(f'<span style="color:{cor_equipe}; font-size:18px">{equipe}</span>', unsafe_allow_html=True)

    jogos = gerar_jogos(grupos)

    st.write("\nJogos Gerados:")
    for nome_grupo, jogos_grupo in jogos.items():
        st.subheader(f"Jogos do {nome_grupo}:")
        for idx, jogo in enumerate(jogos_grupo, start=1):
            equipe_1 = jogo[0]
            equipe_2 = jogo[1]
            st.write(f"Jogo {idx}: {equipe_1} vs {equipe_2}")
            placar_equipe_1 = st.number_input(f"Placar de {equipe_1} ({nome_grupo})", min_value=0, step=1, key=f"{nome_grupo}_{equipe_1}")
            placar_equipe_2 = st.number_input(f"Placar de {equipe_2} ({nome_grupo})", min_value=0, step=1, key=f"{nome_grupo}_{equipe_2}")

if __name__ == "__main__":
    main()