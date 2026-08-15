from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import csv
import os


arquivos = {
    "HBB": "data/HBB_NM_000518.5.gb",
    "HBA1": "data/HBA1_NM_000558.5.gb",
    "VHL": "data/VHL_NM_000551.3.gb"
}

os.makedirs("../resultados", exist_ok=True)

arquivo_saida = "resultados/perfil_molecular.csv"

campos = [
    "Gene",
    "Transcript",
    "Protein_ID",
    "Produto",
    "CDS_nt",
    "RNA_nt",
    "Protein_aa",
    "Molecular_Weight_Da",
    "pI",
    "Aromaticity",
    "Instability_Index",
    "GRAVY",
    "Cys",
    "His",
    "Gly",
    "Pro",
    "Trp",
    "Tyr"
]


resultados = []


for gene, arquivo in arquivos.items():

    registro = SeqIO.read(arquivo, "genbank")

    transcript = registro.id

    for feature in registro.features:

        if feature.type == "CDS":

            cds = feature.extract(registro.seq)

            rna = str(cds).replace("T", "U")

            proteina = feature.qualifiers.get(
                "translation",
                [str(cds.translate()).rstrip("*")]
            )[0]

            # Remove o STOP caso esteja presente
            proteina = proteina.rstrip("*")

            analise = ProteinAnalysis(proteina)

            protein_id = feature.qualifiers.get(
                "protein_id",
                ["Não informado"]
            )[0]

            produto = feature.qualifiers.get(
                "product",
                ["Não informado"]
            )[0]

            resultados.append({
                "Gene": gene,
                "Transcript": transcript,
                "Protein_ID": protein_id,
                "Produto": produto,
                "CDS_nt": len(cds),
                "RNA_nt": len(rna),
                "Protein_aa": len(proteina),
                "Molecular_Weight_Da": round(
                    analise.molecular_weight(), 2
                ),
                "pI": round(
                    analise.isoelectric_point(), 2
                ),
                "Aromaticity": round(
                    analise.aromaticity(), 4
                ),
                "Instability_Index": round(
                    analise.instability_index(), 2
                ),
                "GRAVY": round(
                    analise.gravy(), 4
                ),
                "Cys": proteina.count("C"),
                "His": proteina.count("H"),
                "Gly": proteina.count("G"),
                "Pro": proteina.count("P"),
                "Trp": proteina.count("W"),
                "Tyr": proteina.count("Y")
            })

            break


with open(
    arquivo_saida,
    "w",
    newline="",
    encoding="utf-8"
) as arquivo:

    escritor = csv.DictWriter(
        arquivo,
        fieldnames=campos
    )

    escritor.writeheader()
    escritor.writerows(resultados)


print("=" * 60)
print("CSV GERADO COM SUCESSO")
print("=" * 60)

print(f"\nArquivo:")
print(arquivo_saida)

print(f"\nNúmero de genes analisados: {len(resultados)}")

print("\nGenes:")
for resultado in resultados:
    print(
        f"- {resultado['Gene']}: "
        f"{resultado['Protein_aa']} aa"
    )