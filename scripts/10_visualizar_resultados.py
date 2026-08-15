import csv
from pathlib import Path

import matplotlib.pyplot as plt


# ============================================================
# CONFIGURAÇÃO DO PROJETO
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_CSV = BASE_DIR / "resultados" / "perfil_molecular_final.csv"
PASTA_FIGURAS = BASE_DIR / "resultados" / "figuras"

# Criar a pasta de figuras, caso ainda não exista
PASTA_FIGURAS.mkdir(parents=True, exist_ok=True)


# ============================================================
# LEITURA DOS DADOS
# ============================================================

with open(ARQUIVO_CSV, newline="", encoding="utf-8") as arquivo:
    dados = list(csv.DictReader(arquivo))


# Extrair informações para os gráficos
genes = [linha["Gene"] for linha in dados]
comprimentos = [int(linha["Protein_aa"]) for linha in dados]
pesos = [float(linha["Molecular_Weight_Da"]) for linha in dados]
pis = [float(linha["pI"]) for linha in dados]
gravys = [float(linha["GRAVY"]) for linha in dados]


# ============================================================
# FUNÇÃO PARA PADRONIZAR OS GRÁFICOS
# ============================================================

def configurar_grafico(titulo, xlabel, ylabel):
    plt.figure(figsize=(9, 6))

    plt.title(
        titulo,
        fontsize=14,
        fontweight="bold",
        pad=15
    )

    plt.xlabel(
        xlabel,
        fontsize=11
    )

    plt.ylabel(
        ylabel,
        fontsize=11
    )

    plt.grid(
        axis="y",
        linestyle="--",
        linewidth=0.6,
        alpha=0.5
    )

    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    plt.tight_layout()


# ============================================================
# 1. COMPRIMENTO DAS PROTEÍNAS
# ============================================================

configurar_grafico(
    "Comprimento das proteínas",
    "Gene",
    "Número de aminoácidos"
)

barras = plt.bar(genes, comprimentos)

for barra, valor in zip(barras, comprimentos):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height(),
        f"{valor}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.savefig(
    PASTA_FIGURAS / "comprimento_proteinas.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 2. PESO MOLECULAR
# ============================================================

configurar_grafico(
    "Peso molecular das proteínas",
    "Gene",
    "Peso molecular (Da)"
)

barras = plt.bar(genes, pesos)

for barra, valor in zip(barras, pesos):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height(),
        f"{valor:,.0f}",
        ha="center",
        va="bottom",
        fontsize=9,
        rotation=0
    )

plt.savefig(
    PASTA_FIGURAS / "peso_molecular.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 3. PONTO ISOELÉTRICO
# ============================================================

configurar_grafico(
    "Ponto isoelétrico das proteínas",
    "Gene",
    "Ponto isoelétrico (pI)"
)

barras = plt.bar(genes, pis)

for barra, valor in zip(barras, pis):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height(),
        f"{valor:.2f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.savefig(
    PASTA_FIGURAS / "ponto_isoeletrico.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 4. GRAVY
# ============================================================

configurar_grafico(
    "Perfil de hidropaticidade das proteínas",
    "Gene",
    "GRAVY"
)

barras = plt.bar(genes, gravys)

# Linha de referência em GRAVY = 0
plt.axhline(
    0,
    linewidth=0.8
)

for barra, valor in zip(barras, gravys):
    deslocamento = 0.03 if valor >= 0 else -0.03

    plt.text(
        barra.get_x() + barra.get_width() / 2,
        valor + deslocamento,
        f"{valor:.2f}",
        ha="center",
        va="bottom" if valor >= 0 else "top",
        fontsize=9
    )

plt.savefig(
    PASTA_FIGURAS / "gravy.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# FINALIZAÇÃO
# ============================================================

print("Visualizações refinadas com sucesso.")
print(f"Arquivos salvos em: {PASTA_FIGURAS}")