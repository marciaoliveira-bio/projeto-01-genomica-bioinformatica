from Bio import SeqIO
from Bio.Align import PairwiseAligner
from pathlib import Path


# ============================================================
# CONFIGURAÇÃO DOS CAMINHOS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

VALIDACAO_DIR = BASE_DIR / "validacao"

VALIDACAO_DIR.mkdir(exist_ok=True)

ARQUIVO_SAIDA = VALIDACAO_DIR / "validacao_final.txt"


arquivos = {
    "HBB": DATA_DIR / "HBB_NM_000518.5.gb",
    "HBA1": DATA_DIR / "HBA1_NM_000558.5.gb",
    "VHL": DATA_DIR / "VHL_NM_000551.3.gb"
}


# ============================================================
# OBTER SEQUÊNCIA PROTEICA
# ============================================================

def obter_proteina(arquivo):

    registro = SeqIO.read(arquivo, "genbank")

    for feature in registro.features:

        if feature.type == "CDS":

            proteina = feature.qualifiers.get("translation")

            if proteina:
                return proteina[0].rstrip("*")

            cds = feature.extract(registro.seq)

            return str(cds.translate()).rstrip("*")

    raise ValueError("Nenhuma CDS encontrada.")


# ============================================================
# COMPARAÇÃO DAS PROTEÍNAS
# ============================================================

def comparar(seq1, seq2):

    alinhador = PairwiseAligner()

    alinhador.mode = "global"

    alinhador.match_score = 2
    alinhador.mismatch_score = -1
    alinhador.open_gap_score = -2
    alinhador.extend_gap_score = -0.5

    alinhamentos = alinhador.align(seq1, seq2)

    alinhamento = alinhamentos[0]

    matches = 0
    aligned_positions = 0

    for bloco1, bloco2 in zip(
        alinhamento.aligned[0],
        alinhamento.aligned[1]
    ):

        inicio1, fim1 = bloco1
        inicio2, fim2 = bloco2

        tamanho = min(
            fim1 - inicio1,
            fim2 - inicio2
        )

        aligned_positions += tamanho

        for i in range(tamanho):

            if seq1[inicio1 + i] == seq2[inicio2 + i]:
                matches += 1

    if aligned_positions == 0:
        raise ValueError(
            "Nenhuma posição válida foi encontrada no alinhamento."
        )

    identity = (
        matches / aligned_positions
    ) * 100

    cobertura1 = (
        aligned_positions / len(seq1)
    ) * 100

    cobertura2 = (
        aligned_positions / len(seq2)
    ) * 100

    return (
        matches,
        aligned_positions,
        identity,
        cobertura1,
        cobertura2
    )


# ============================================================
# REGISTRO DOS RESULTADOS
# ============================================================

resultados = []


def registrar(texto=""):

    print(texto)
    resultados.append(texto)


# ============================================================
# INÍCIO DA VALIDAÇÃO
# ============================================================

registrar("=" * 70)
registrar("VALIDAÇÃO POR ALINHAMENTO PROTEICO")
registrar("=" * 70)

registrar("\nMETODOLOGIA")
registrar("-" * 70)
registrar("Alinhamento: global")
registrar("Algoritmo: PairwiseAligner (Biopython)")
registrar("Match score: 2")
registrar("Mismatch score: -1")
registrar("Gap opening: -2")
registrar("Gap extension: -0.5")
registrar(
    "Identidade: posições idênticas / posições alinhadas × 100"
)
registrar(
    "Cobertura: posições alinhadas / comprimento da sequência × 100"
)

proteinas = {}


for gene, arquivo in arquivos.items():

    proteinas[gene] = obter_proteina(arquivo)

    registrar(
        f"\n{gene}: {len(proteinas[gene])} aa"
    )


# ============================================================
# COMPARAÇÕES
# ============================================================

comparacoes = [
    ("HBB", "HBA1"),
    ("HBB", "VHL"),
    ("HBA1", "VHL")
]


for g1, g2 in comparacoes:

    (
        matches,
        aligned_positions,
        identidade,
        cobertura1,
        cobertura2
    ) = comparar(
        proteinas[g1],
        proteinas[g2]
    )

    registrar("\n" + "-" * 70)
    registrar(f"{g1} × {g2}")
    registrar("-" * 70)

    registrar(
        f"Tamanho {g1}: {len(proteinas[g1])} aa"
    )

    registrar(
        f"Tamanho {g2}: {len(proteinas[g2])} aa"
    )

    registrar(
        f"Posições idênticas: {matches}"
    )

    registrar(
        f"Posições alinhadas: {aligned_positions}"
    )

    registrar(
        f"Identidade: {identidade:.2f}%"
    )

    registrar(
        f"Cobertura {g1}: {cobertura1:.2f}%"
    )

    registrar(
        f"Cobertura {g2}: {cobertura2:.2f}%"
    )

    registrar(
        "Interpretação: comparação realizada por "
        "alinhamento global de sequências proteicas."
    )


# ============================================================
# FINALIZAÇÃO
# ============================================================

registrar("\n" + "=" * 70)
registrar("VALIDAÇÃO CONCLUÍDA")
registrar("=" * 70)


# ============================================================
# SALVAR RESULTADO
# ============================================================

with open(
    ARQUIVO_SAIDA,
    "w",
    encoding="utf-8"
) as arquivo:

    arquivo.write(
        "\n".join(resultados)
    )


print()
print(
    f"Resultado salvo em: {ARQUIVO_SAIDA}"
)