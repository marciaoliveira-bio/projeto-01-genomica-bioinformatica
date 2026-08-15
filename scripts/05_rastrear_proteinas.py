from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from pathlib import Path


# ============================================================
# CONFIGURAÇÃO DOS CAMINHOS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


arquivos = {
    "HBB": DATA_DIR / "HBB_NM_000518.5.gb",
    "HBA1": DATA_DIR / "HBA1_NM_000558.5.gb",
    "VHL": DATA_DIR / "VHL_NM_000551.3.gb"
}


# ============================================================
# ANÁLISE DAS PROTEÍNAS
# ============================================================

for gene, arquivo in arquivos.items():

    registro = SeqIO.read(arquivo, "genbank")

    for feature in registro.features:

        if feature.type == "CDS":

            # Obtém a sequência proteica
            proteina = feature.qualifiers.get(
                "translation",
                [None]
            )[0]

            if not proteina:
                cds = feature.extract(registro.seq)
                proteina = str(cds.translate()).rstrip("*")

            # Remove o STOP caso esteja presente
            proteina = proteina.rstrip("*")

            analise = ProteinAnalysis(proteina)

            print("\n" + "=" * 60)
            print(f"GENE: {gene}")
            print("=" * 60)

            print(f"Proteína: {proteina}")
            print(f"Tamanho: {len(proteina)} aa")

            print("\n--- PERFIL FÍSICO-QUÍMICO ---")

            print(
                f"Peso molecular: "
                f"{analise.molecular_weight():.2f} Da"
            )

            print(
                f"Ponto isoelétrico (pI): "
                f"{analise.isoelectric_point():.2f}"
            )

            print(
                f"Aromaticidade: "
                f"{analise.aromaticity():.4f}"
            )

            print(
                f"Instabilidade: "
                f"{analise.instability_index():.2f}"
            )

            print(
                f"GRAVY: "
                f"{analise.gravy():.4f}"
            )

            print("\n--- COMPOSIÇÃO DE AMINOÁCIDOS ---")

            composicao = analise.amino_acids_percent

            for aa, percentual in sorted(composicao.items()):

                if percentual > 0:
                    print(f"{aa}: {percentual:.2f}%")

            print("\n--- MOTIVOS / CARACTERÍSTICAS ---")

            motivos = {
                "Histidinas (H)": proteina.count("H"),
                "Cisteínas (C)": proteina.count("C"),
                "Glicinas (G)": proteina.count("G"),
                "Prolinas (P)": proteina.count("P"),
                "Triptofanos (W)": proteina.count("W"),
                "Tirosinas (Y)": proteina.count("Y")
            }

            for nome, quantidade in motivos.items():
                print(f"{nome}: {quantidade}")

            break