"""
Diagrama Sankey para Justificação de Seleção de Variáveis - Clustering
=========================================================================
Autor: Análise de Clustering de Dataset Acadêmico
Data: 11/11/2025

Este script cria um diagrama Sankey que visualiza o processo de filtragem
de variáveis desde o dataset completo (28 variáveis) até as 7 variáveis
selecionadas para análise de clustering.
"""

import plotly.graph_objects as go

# ========================================================================
# DEFINIÇÃO DOS CRITÉRIOS DE FILTRAGEM
# ========================================================================

criterios = {
    "Etapa 1 - Tipo de Dado": {
        "Categóricas": [
            "nome",
            "sexo",
            "formacao",
            "vinculo",
            "categoria",
            "classe_funcional",
            "lotacao",
        ],
        "Numéricas": ["todas as outras 21 variáveis"],
    },
    "Etapa 2 - Natureza": {
        "Identificadores/Contexto": ["id_turma", "ano", "periodo", "ano_admissao"],
        "Métricas Impessoais": ["17 variáveis restantes"],
    },
    "Etapa 3 - Completude": {
        "Dados Incompletos": ["autoavaliacao_aluno_media", "autoavaliacao_aluno_DP"],
        "Dados Completos": ["15 variáveis restantes"],
    },
    "Etapa 4 - Redundância": {
        "Redundantes": [
            "qtd_aprovado",
            "qtd_desistencia",
            "qtd_reprovado_por_média_e_por_faltas",
            "qtd_trancado",
            "qtd_aprovado_por_nota",
            "qtd_reprovado",
            "qtd_reprovado_por_faltas",
            "qtd_reprovado_por_nota_e_falta",
            "qtd_reprovado_por_nota",
        ],
        "Selecionadas": [
            "qtd_discentes",
            "proporcao_aprovados",
            "media_final_geral",
            "postura_profissional_media",
            "postura_profissional_DP",
            "atuacao_profissional_media",
            "atuacao_profissional_DP",
        ],
    },
}

# ========================================================================
# ESTRUTURA DO DIAGRAMA SANKEY
# ========================================================================

# Nós do diagrama (cada estágio do processo)
nodes = [
    "<b>Dataset <br>Completo <br>(28)</b>",  # 0 - Origem
    "Categóricas (7)",  # 1 - Divisão por tipo
    "<b>Numéricas (21)</b>",  # 2 - Divisão por tipo
    "Identificadores <br>Pessoais (7)",  # 3 - Fim: descartadas
    "Identificadores/<br>Contexto (4)",  # 4 - Subdivisão numérica
    "<b>Métricas<br>Impessoais (17)</b>",  # 5 - Subdivisão numérica
    "Contexto (4)",  # 6 - Fim: descartadas
    "Dados<br>Incompletos (2)",  # 7 - Divisão por completude
    "<b>Dados<br>Completos<br>(15)</b>",  # 8 - Divisão por completude
    "(2)",  # 9 - Fim: descartadas
    "Redundância (8)",  # 10 - Fim: descartadas
    "<b>Variáveis <br>Selecionadas <br> (7)</b>",  # 11 - Fim: selecionadas
]

# Conexões entre os nós (source -> target com valor)
links = [
    # Etapa 1: Separação por tipo de dado
    {"source": 0, "target": 1, "value": 7},  # 28 -> Categóricas (7)
    {"source": 0, "target": 2, "value": 21},  # 28 -> Numéricas (21)
    # Etapa 1: Descarte de categóricas
    {"source": 1, "target": 3, "value": 7},  # Categóricas -> Descartadas
    # Etapa 2: Separação por natureza (numéricas)
    {"source": 2, "target": 4, "value": 4},  # Numéricas -> Identificadores (4)
    {"source": 2, "target": 5, "value": 17},  # Numéricas -> Métricas (17)
    # Etapa 2: Descarte de identificadores
    {"source": 4, "target": 6, "value": 4},  # Identificadores -> Descartadas
    # Etapa 3: Separação por completude
    {"source": 5, "target": 7, "value": 2},  # Métricas -> Incompletos (2)
    {"source": 5, "target": 8, "value": 15},  # Métricas -> Completos (15)
    # Etapa 3: Descarte por missing values
    {"source": 7, "target": 9, "value": 2},  # Incompletos -> Descartadas
    # Etapa 4: Filtragem final por redundância
    {"source": 8, "target": 10, "value": 8},  # Completos -> Redundantes
    {"source": 8, "target": 11, "value": 7},  # Completos -> Selecionadas ✓
]

# ========================================================================
# CONFIGURAÇÃO DE CORES
# ========================================================================

# Cores para os nós (seguindo lógica de semáforo + destaque)
node_colors = [
    "#3498db",  # 0 - Dataset completo (azul inicial)
    "#f39c12",  # 1 - Categóricas (laranja - em análise)
    "#2ecc71",  # 2 - Numéricas (verde - continua)
    "#e74c3c",  # 3 - Descartadas pessoais (vermelho)
    "#f39c12",  # 4 - Identificadores (laranja - em análise)
    "#2ecc71",  # 5 - Métricas impessoais (verde - continua)
    "#e74c3c",  # 6 - Descartadas contexto (vermelho)
    "#f39c12",  # 7 - Dados incompletos (laranja - em análise)
    "#2ecc71",  # 8 - Dados completos (verde - continua)
    "#e74c3c",  # 9 - Descartadas missing (vermelho)
    "#e74c3c",  # 10 - Descartadas redundância (vermelho)
    "#27ae60",  # 11 - Selecionadas (verde escuro - destaque final)
]

# Cores para os links (com transparência para melhor visualização)
link_colors = [
    "rgba(52, 152, 219, 0.3)",  # 0->1 (azul)
    "rgba(52, 152, 219, 0.3)",  # 0->2 (azul)
    "rgba(243, 156, 18, 0.3)",  # 1->3 (laranja)
    "rgba(46, 204, 113, 0.3)",  # 2->4 (verde)
    "rgba(46, 204, 113, 0.3)",  # 2->5 (verde)
    "rgba(243, 156, 18, 0.3)",  # 4->6 (laranja)
    "rgba(46, 204, 113, 0.3)",  # 5->7 (verde)
    "rgba(46, 204, 113, 0.3)",  # 5->8 (verde)
    "rgba(243, 156, 18, 0.3)",  # 7->9 (laranja)
    "rgba(243, 156, 18, 0.3)",  # 8->10 (verde)
    "rgba(46, 204, 113, 0.5)",  # 8->11 (verde mais opaco - destaque)
]

# ========================================================================
# CRIAÇÃO DO DIAGRAMA SANKEY
# ========================================================================

fig = go.Figure(
    data=[
        go.Sankey(
            arrangement="snap",  # Try 'snap', 'perpendicular', 'freeform', or 'fixed'
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=nodes,
                color=node_colors,
                # Explicit positioning (0 to 1 scale)
                x=[
                    0.05,  # 0 - Dataset
                    0.25,
                    0.25,  # 1,2 - Categóricas, Numéricas
                    0.95,  # 3 - Descartadas pessoais
                    0.45,
                    0.45,  # 4,5 - Identificadores, Métricas
                    0.95,  # 6 - Descartadas contexto
                    0.65,
                    0.65,  # 7,8 - Incompletos, Completos
                    0.95,  # 9 - Descartadas missing
                    0.95,
                    0.95,
                ],  # 10,11 - Redundantes, Selecionadas
                y=[
                    0.5,  # 0 - Dataset (centro)
                    0.7,  # 1,2 - Cat (baixo), Num (alto)
                    0.2,
                    0.2,  # 3 - Descartadas pessoais (embaixo)
                    0.6,
                    0.15,  # 4,5 - Ident (meio-baixo), Métricas (alto)
                    0.15,  # 6 - Descartadas contexto
                    0.5,
                    0.1,  # 7,8 - Incomp (meio), Compl (muito alto)
                    0.08,  # 9 - Descartadas missing
                    0.06,# 10 - Redundantes (baixo)
                    0.01,# 11 - Selecionadas (topo)
                ],  
                hoverlabel=dict(font=dict(size=16)),
            ),
            link=dict(
                source=[link["source"] for link in links],
                target=[link["target"] for link in links],
                value=[link["value"] for link in links],
                color=link_colors,
            ),
        )
    ]
)

# Modifique a configuração do layout para aumentar o tamanho da fonte geral
fig.update_layout(
    font=dict(size=30, family="Arial, sans-serif"),  # Fonte geral maior
    height=770,
    width=1320,
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=20, r=20, t=60, b=20),
)

# ========================================================================
# SALVAR E EXIBIR
# ========================================================================

# Salvar como HTML interativo
fig.write_html("sankey_clustering_variaveis.html")
print("✓ Diagrama Sankey salvo como 'sankey_clustering_variaveis.html'")

# Exibir o diagrama (em ambiente interativo)
fig.show()

print("\n" + "=" * 70)
print("VARIÁVEIS FINAIS SELECIONADAS")
print("=" * 70)
print("1. qtd_discentes               - Tamanho da turma")
print("2. proporcao_aprovados         - Taxa de aprovação (derivada)")
print("3. media_final_geral           - Desempenho médio da turma")
print("4. postura_profissional_media  - Avaliação média: postura")
print("5. postura_profissional_DP     - Dispersão: postura")
print("6. atuacao_profissional_media  - Avaliação média: atuação")
print("7. atuacao_profissional_DP     - Dispersão: atuação")
print("=" * 70)

print("\n" + "=" * 70)
print("LEGENDA DE CORES")
print("=" * 70)
print("🔵 Azul: Dataset original")
print("🟢 Verde: Variáveis mantidas no processo")
print("🟠 Laranja: Variáveis em análise/transição")
print("🔴 Vermelho: Variáveis descartadas")
print("🟢 Verde escuro: Variáveis finais selecionadas para clustering")
print("=" * 70)
