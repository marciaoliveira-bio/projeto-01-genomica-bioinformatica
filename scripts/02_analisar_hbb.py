from Bio import SeqIO

# Ler o arquivo FASTA
record = SeqIO.read("data/HBB_NM_000518.5.fasta", "fasta")

print("ID:", record.id)
print("Descrição:", record.description)
print("Comprimento:", len(record.seq))

# Ler o arquivo GenBank
genbank_record = SeqIO.read("data/HBB_NM_000518.5.gb", "genbank")

# Procurar a CDS
for feature in genbank_record.features:
    if feature.type == "CDS":
        print("\nCDS encontrada!")
        print("Localização:", feature.location)
        print("Produto:", feature.qualifiers.get("product"))
        print("Protein ID:", feature.qualifiers.get("protein_id"))

        # Extrair a CDS
        cds_sequence = feature.extract(genbank_record.seq)

        print("Tamanho da CDS:", len(cds_sequence))
        print("Sequência CDS:", cds_sequence)

        # Traduzir a CDS
        protein_sequence = cds_sequence.translate()

        # Verificar o códon de parada
        if protein_sequence.endswith("*"):
            protein_without_stop = protein_sequence[:-1]
            stop_codon = "*"
        else:
            protein_without_stop = protein_sequence
            stop_codon = "Não identificado"

        print("Tamanho da proteína incluindo STOP:", len(protein_sequence))
        print("Tamanho da proteína em aminoácidos:", len(protein_without_stop))
        print("Códon de parada:", stop_codon)
        print("Proteína:", protein_without_stop)