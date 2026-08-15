from Bio import SeqIO
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
# ANÁLISE DOS GENES
# ============================================================

for gene, arquivo in arquivos.items():

    print("\n" + "=" * 60)
    print(f"GENE: {gene}")
    print("=" * 60)

    registro = SeqIO.read(arquivo, "genbank")

    print(f"Descrição: {registro.description}")
    print(f"Tamanho do mRNA: {len(registro.seq)} nt")

    cds_encontrada = False

    for feature in registro.features:

        if feature.type == "CDS":

            cds_encontrada = True

            cds = feature.extract(registro.seq)

            # ------------------------------------------------
            # Transcrição computacional DNA → RNA
            # ------------------------------------------------

            rna = str(cds).replace("T", "U")

            # ------------------------------------------------
            # Tradução DNA → proteína
            # ------------------------------------------------

            proteina = feature.qualifiers.get(
                "translation",
                [str(cds.translate())]
            )[0]

            proteina = proteina.rstrip("*")

            produto = feature.qualifiers.get(
                "product",
                ["Não informado"]
            )[0]

            protein_id = feature.qualifiers.get(
                "protein_id",
                ["Não informado"]
            )[0]

            print("\nCDS encontrada!")
            print(f"Localização: {feature.location}")
            print(f"Produto: {produto}")
            print(f"Protein ID: {protein_id}")
            print(f"Tamanho da CDS: {len(cds)} nt")
            print(f"Tamanho do RNA: {len(rna)} nt")
            print(f"Tamanho da proteína: {len(proteina)} aa")

            print(f"\nCDS:\n{cds}")
            print(f"\nRNA:\n{rna}")
            print(f"\nProteína:\n{proteina}")

            break

    if not cds_encontrada:

        print("Nenhuma CDS encontrada!")