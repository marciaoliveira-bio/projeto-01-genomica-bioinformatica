from Bio import Entrez, SeqIO

Entrez.email = "oliveira.marcia0507@gmail.com"

alvos = {
    "HBA1": "NM_000558.5",
    "VHL": "NM_000551.3"
}

for gene, accession in alvos.items():

    print(f"\nBuscando {gene} - {accession}...")

    # Buscar registro GenBank
    handle = Entrez.efetch(
        db="nuccore",
        id=accession,
        rettype="gb",
        retmode="text"
    )

    registro = SeqIO.read(handle, "genbank")
    handle.close()

    arquivo_gb = f"data/{gene}_{accession}.gb"

    with open(arquivo_gb, "w", encoding="utf-8") as arquivo:
        SeqIO.write(registro, arquivo, "genbank")

    print(f"{gene} GenBank salvo em: {arquivo_gb}")

    # Buscar registro FASTA
    handle = Entrez.efetch(
        db="nuccore",
        id=accession,
        rettype="fasta",
        retmode="text"
    )

    registro_fasta = SeqIO.read(handle, "fasta")
    handle.close()

    arquivo_fasta = f"data/{gene}_{accession}.fasta"

    with open(arquivo_fasta, "w", encoding="utf-8") as arquivo:
        SeqIO.write(registro_fasta, arquivo, "fasta")

    print(f"{gene} FASTA salvo em: {arquivo_fasta}")

print("\nBusca dos genes-alvo concluída.")