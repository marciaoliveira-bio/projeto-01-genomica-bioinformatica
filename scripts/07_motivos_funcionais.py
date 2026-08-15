from Bio import SeqIO
import re


arquivos = {
    "HBB": "data/HBB_NM_000518.5.gb",
    "HBA1": "data/HBA1_NM_000558.5.gb",
    "VHL": "data/VHL_NM_000551.3.gb"
}

def procurar_bc_box(proteina):
    """
    BC-box:
    [APST]-L-x3-C-x3-[AILV]
    """

    padrao = r"[APST]L...C...[AILV]"

    encontrados = []

    for resultado in re.finditer(padrao, proteina):
        inicio = resultado.start() + 1
        fim = resultado.end()

        encontrados.append({
            "sequencia": resultado.group(),
            "inicio": inicio,
            "fim": fim
        })

    return encontrados


def procurar_histidinas(proteina):

    encontrados = []

    for i, aa in enumerate(proteina):

        if aa == "H":

            encontrados.append(i + 1)

    return encontrados


print("=" * 70)
print("RASTREAMENTO DE MOTIVOS FUNCIONAIS")
print("=" * 70)


for gene, arquivo in arquivos.items():

    registro = SeqIO.read(arquivo, "genbank")

    for feature in registro.features:

        if feature.type == "CDS":

            proteina = feature.qualifiers.get(
                "translation",
                [str(feature.extract(registro.seq).translate()).rstrip("*")]
            )[0]

            proteina = proteina.rstrip("*")

            print("\n" + "=" * 70)
            print(f"GENE: {gene}")
            print("=" * 70)

            print(f"Proteína: {proteina}")
            print(f"Tamanho: {len(proteina)} aa")

            # --------------------------------------------------
            # HBB
            # --------------------------------------------------

            if gene == "HBB":

                histidinas = procurar_histidinas(proteina)

                print("\n--- ASSINATURA FUNCIONAL ---")
                print("Função: subunidade beta da hemoglobina")
                print("Ligação: heme / oxigênio")
                print(f"Resíduos de histidina encontrados: {histidinas}")
                print("Status: assinatura compatível com proteína globina")

            # --------------------------------------------------
            # HBA1
            # --------------------------------------------------

            elif gene == "HBA1":

                histidinas = procurar_histidinas(proteina)

                print("\n--- ASSINATURA FUNCIONAL ---")
                print("Função: subunidade alfa da hemoglobina")
                print("Ligação: heme / oxigênio")
                print(f"Resíduos de histidina encontrados: {histidinas}")
                print("Status: assinatura compatível com proteína globina")

            # --------------------------------------------------
            # VHL
            # --------------------------------------------------

            elif gene == "VHL":

                bc_box = procurar_bc_box(proteina)

                print("\n--- ASSINATURAS FUNCIONAIS ---")

                if bc_box:

                    print("BC-box encontrado:")

                    for motivo in bc_box:

                        print(
                            f"  Sequência: {motivo['sequencia']}"
                        )

                        print(
                            f"  Posição: "
                            f"{motivo['inicio']}-{motivo['fim']}"
                        )

                else:

                    print("BC-box não encontrado pelo padrão utilizado.")

                print("\nDomínio funcional:")
                print("Proteína VHL / domínio VHL")
                print("Função: recrutamento de HIF para complexo E3 ubiquitina-ligase")

            break


print("\n" + "=" * 70)
print("RASTREAMENTO CONCLUÍDO")
print("=" * 70)