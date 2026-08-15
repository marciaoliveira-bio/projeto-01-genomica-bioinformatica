# Projeto 01 — Análise Genômica e Bioinformática

Projeto educacional desenvolvido para aplicar conceitos de Biologia Molecular, Genética e Bioinformática na análise de sequências gênicas e proteicas humanas.

O projeto foi desenvolvido progressivamente utilizando Python e Biopython, com foco na construção de um fluxo reprodutível para obtenção, análise, organização e comparação de sequências biológicas.

## Objetivo

Desenvolver um pipeline introdutório de análise molecular utilizando os genes:

- **HBB** — hemoglobin subunit beta
- **HBA1** — hemoglobin subunit alpha 1
- **VHL** — von Hippel-Lindau tumor suppressor

O projeto inclui etapas de obtenção de sequências, identificação de CDS, tradução para sequência proteica, análise físico-química, rastreamento de características funcionais, organização dos resultados em tabelas e validação por alinhamento proteico.

## Estrutura do projeto

```text
projeto_01_genomica_bioinformatica/
├── data/
│   ├── HBB_NM_000518.5.fasta
│   ├── HBB_NM_000518.5.gb
│   ├── HBA1_NM_000558.5.fasta
│   ├── HBA1_NM_000558.5.gb
│   ├── VHL_NM_000551.3.fasta
│   └── VHL_NM_000551.3.gb
│
├── evidencias/
│   └── BLASTp_HBB.txt
│
├── scripts/
│   ├── 01_buscar_hbb.py
│   ├── 02_analisar_hbb.py
│   ├── 03_buscar_alvos.py
│   ├── 04_analisar_alvos.py
│   ├── 05_rastrear_proteinas.py
│   ├── 06_gerar_csv.py
│   ├── 07_motivos_funcionais.py
│   ├── 08_atualizar_csv.py
│   └── 09_validar_homologia.py
│
├── resultados/
│   ├── perfil_molecular.csv
│   └── perfil_molecular_final.csv
│
├── validacao/
│   └── validacao_final.txt
│
├── README.md
└── requirements.txt

Etapas da análise
1. Obtenção das sequências

Os scripts iniciais realizam a obtenção das sequências de referência dos genes selecionados e armazenam os arquivos em formatos FASTA e GenBank.

2. Análise das sequências

O projeto identifica a região codificante (CDS), determina seu comprimento e realiza a tradução para a sequência proteica correspondente.

3. Análise físico-química

As proteínas são analisadas quanto a:

comprimento;
peso molecular;
ponto isoelétrico (pI);
aromaticidade;
índice de instabilidade;
GRAVY;
composição de aminoácidos.
4. Características funcionais

São avaliadas características relacionadas às proteínas analisadas.

Para HBB e HBA1, o projeto registra a compatibilidade com proteínas da família das globinas.

Para VHL, é registrado o motivo funcional utilizado na análise:

TLKERCLQVV
5. Organização dos resultados

Os resultados são organizados em arquivos CSV para facilitar a inspeção e posterior análise.

O arquivo perfil_molecular_final.csv reúne informações moleculares e anotações funcionais dos genes analisados.

6. Validação por alinhamento proteico

O script 09_validar_homologia.py realiza comparações entre:

HBB × HBA1
HBB × VHL
HBA1 × VHL

As comparações são realizadas utilizando alinhamento global com PairwiseAligner, do Biopython.

A identidade é calculada como:

identidade = posições idênticas / posições alinhadas × 100

A cobertura é calculada separadamente para cada sequência:

cobertura = posições alinhadas / comprimento da sequência × 100
Parâmetros utilizados
Tipo de alinhamento: global
Match score: 2
Mismatch score: -1
Gap opening: -2
Gap extension: -0.5

Os resultados da validação são armazenados em:

validacao/validacao_final.txt
Resultados atuais
Comparação    Identidade    Cobertura 1    Cobertura 2
HBB × HBA1    53.03%    89.80%    92.96%
HBB × VHL    52.63%    77.55%    53.52%
HBA1 × VHL    47.50%    84.51%    56.34%

Esses valores representam os resultados obtidos sob os parâmetros definidos no projeto e não devem ser interpretados isoladamente como evidência de homologia evolutiva.

Tecnologias utilizadas
Python 3.13
Biopython 1.88
CSV
PairwiseAligner
PowerShell
Git/GitHub
Objetivo de aprendizagem

Este projeto faz parte da construção progressiva de competências em:

Biologia Molecular;
Genética;
análise de sequências;
programação em Python;
bioinformática;
análise de proteínas;
organização de dados biológicos;
reprodutibilidade computacional.

O projeto será expandido posteriormente com novas análises e ferramentas de bioinformática.

Observação

Este é um projeto educacional desenvolvido para documentar o processo de aprendizagem e aplicação prática de conceitos de bioinformática.

As análises e interpretações devem ser consideradas dentro dos parâmetros e limitações metodológicas descritos neste repositório.