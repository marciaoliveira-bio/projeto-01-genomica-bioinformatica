import csv
import os


arquivo_entrada = "resultados/perfil_molecular.csv"
arquivo_saida = "resultados/perfil_molecular_final.csv"


motivos = {
    "HBB": {
        "Functional_Annotation": "Hemoglobina beta / ligacao ao heme",
        "Functional_Motif": "Globina",
        "Motif_Position": "Nao determinado"
    },

    "HBA1": {
        "Functional_Annotation": "Hemoglobina alfa / ligacao ao heme",
        "Functional_Motif": "Globina",
        "Motif_Position": "Nao determinado"
    },

    "VHL": {
        "Functional_Annotation": "Proteina VHL / regulacao de HIF",
        "Functional_Motif": "TLKERCLQVV",
        "Motif_Position": "157-166"
    }
}


with open(
    arquivo_entrada,
    "r",
    encoding="utf-8"
) as arquivo:

    leitor = csv.DictReader(arquivo)

    dados = list(leitor)


novos_campos = [
    "Functional_Annotation",
    "Functional_Motif",
    "Motif_Position"
]


for linha in dados:

    gene = linha["Gene"]

    if gene in motivos:

        linha["Functional_Annotation"] = motivos[gene][
            "Functional_Annotation"
        ]

        linha["Functional_Motif"] = motivos[gene][
            "Functional_Motif"
        ]

        linha["Motif_Position"] = motivos[gene][
            "Motif_Position"
        ]


campos = list(dados[0].keys())


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
    escritor.writerows(dados)


print("=" * 60)
print("CSV FINAL GERADO COM SUCESSO")
print("=" * 60)

print(f"\nArquivo:")
print(arquivo_saida)

print(f"\nGenes registrados: {len(dados)}")

for linha in dados:

    print(
        f"- {linha['Gene']}: "
        f"{linha['Functional_Annotation']}"
    )