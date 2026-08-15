from Bio import Entrez

Entrez.email = "oliveira.marcia0507@gmail.com"

accession = "NM_000518.5"

# 1. Buscar o registro em FASTA
handle = Entrez.efetch(
    db="nuccore",
    id=accession,
    rettype="fasta",
    retmode="text"
)

record = handle.read()
print("Tamanho do FASTA:", len(record))

handle.close()

# 2. Salvar o FASTA
with open("data/HBB_NM_000518.5.fasta", "w", encoding="utf-8") as file:
    file.write(record)

# 3. Buscar o mesmo registro em GenBank
handle = Entrez.efetch(
    db="nuccore",
    id=accession,
    rettype="gb",
    retmode="text"
)

genbank_record = handle.read()
print("Tamanho do GenBank:", len(genbank_record))

handle.close()

# 4. Salvar o GenBank
with open("data/HBB_NM_000518.5.gb", "w", encoding="utf-8") as file:
    file.write(genbank_record)
    
