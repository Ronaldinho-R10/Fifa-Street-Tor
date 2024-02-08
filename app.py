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

# Dicionário com os emojis correspondentes aos países
EMOJIS_EQUIPES = {
    "Alemanha": "🇩🇪",
    "Argentina": "🇦🇷",
    "Austrália": "🇦🇺",
    "Brasil": "🇧🇷",
    "Camarões": "🇨🇲",
    "Coreia do Sul": "🇰🇷",
    "Dinamarca": "🇩🇰",
    "Escócia": "🏴",
    "Espanha": "🇪🇸",
    "Estados Unidos": "🇺🇸",
    "França": "🇫🇷",
    "Grécia": "🇬🇷",
    "Inglaterra": "🏴",
    "República da Irlanda": "🇮🇪",
    "Itália": "🇮🇹",
    "México": "🇲🇽",
    "Nigéria": "🇳🇬",
    "Portugal": "🇵🇹",
    "Chéquia": "🇨🇿",
    "Suécia": "🇸🇪"
}

def cadastrar_equipes():
    equipes_selecionadas = st.multiselect("Selecione as equipes:", options=list(CORES_EQUIPES.keys()), default=list(CORES_EQUIPES.keys()), format_func=lambda equipe: f"{EMOJIS_EQUIPES[equipe]} {equipe}")
    return equipes_selecionadas

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
    st.write("Por favor, selecione as equipes participantes:")

    equipes_selecionadas = cadastrar_equipes()

    grupos = criar_grupos(equipes_selecionadas)

    st.write("\nGrupos Criados:")
    for nome_grupo, equipes_grupo in grupos.items():
        st.write(f"{nome_grupo}:")
        table_data = []
        for equipe in equipes_grupo:
            cor_equipe = CORES_EQUIPES[equipe]
            table_data.append([f'{EMOJIS_EQUIPES[equipe]} {equipe}', f'<span style="color:{cor_equipe}; font-size:20px">{EMOJIS_EQUIPES[equipe]} {equipe}</span>'])
        st.table(table_data)

    jogos = gerar_jogos(grupos)

    st.write("\nJogos Gerados:")
    for idx, jogo in enumerate(jogos, start=1):
        st.write(f"Jogo {idx}: {jogo[0]} vs {jogo[1]}")

if __name__ == "__main__":
    main()
