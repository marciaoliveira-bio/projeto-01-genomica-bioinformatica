# 🧬 Projeto 01 — Genômica e Bioinformática
### Análise de sequências e caracterização molecular de proteínas

> Pipeline introdutório desenvolvido em Python e Biopython para análise, caracterização e comparação de sequências gênicas e proteicas humanas.

Projeto desenvolvido como parte da minha formação prática em Bioinformática, com foco na utilização de Python e Biopython para obtenção, processamento, análise, caracterização e visualização de dados moleculares.

O projeto apresenta um pipeline computacional reprodutível aplicado a sequências de genes humanos, integrando conceitos de Biologia Molecular, Genética, Bioinformática, análise de sequências, análise de proteínas e programação em Python.

---

## 🎯 Objetivo

Desenvolver um pipeline introdutório de análise bioinformática capaz de:

- obter sequências de referência;
- trabalhar com arquivos FASTA e GenBank;
- identificar regiões codificantes (CDS);
- traduzir sequências nucleotídicas em proteínas;
- caracterizar propriedades físico-químicas de proteínas;
- organizar resultados em arquivos CSV;
- comparar sequências proteicas;
- realizar alinhamentos globais;
- calcular identidade e cobertura;
- gerar visualizações gráficas dos resultados.

O projeto foi estruturado priorizando **organização, rastreabilidade e reprodutibilidade computacional**.

---

## 🧬 Genes analisados

Foram analisados três genes humanos:

| **Gene** | **Proteína** | **Contexto biológico** |
|---|---|---|
| **HBB** | Hemoglobina beta | Transporte de oxigênio |
| **HBA1** | Hemoglobina alfa 1 | Transporte de oxigênio |
| **VHL** | Proteína supressora tumoral von Hippel-Lindau | Regulação celular e resposta à hipóxia |

---

## 🔬 Pipeline de análise

O fluxo desenvolvido pode ser representado da seguinte forma:

```text
Sequências de referência
        ↓
Arquivos FASTA / GenBank
        ↓
Identificação da CDS
        ↓
Tradução DNA → proteína
        ↓
Caracterização molecular
        ↓
Análise de características funcionais
        ↓
Organização dos resultados em CSV
        ↓
Comparação entre proteínas
        ↓
Alinhamento global
        ↓
Identidade e cobertura
        ↓
Visualização dos resultados
```

## 📊 Caracterização molecular:

As proteínas foram analisadas utilizando recursos do Biopython.

Foram avaliados parâmetros como:

comprimento da proteína;
peso molecular;
ponto isoelétrico (pI);
aromaticidade;
índice de instabilidade;
GRAVY;
composição de aminoácidos.

Os resultados foram organizados em arquivos CSV para facilitar a comparação entre as proteínas.

O principal arquivo consolidado é:

resultados/perfil_molecular_final.csv

## 📈 Visualização dos resultados:

A etapa final do pipeline utiliza Matplotlib para transformar os resultados tabulares em representações gráficas.

Foram geradas quatro visualizações:

Comprimento das proteínas

Peso molecular

Ponto isoelétrico

GRAVY

As figuras são exportadas em formato PNG para utilização na documentação, apresentação e análise dos resultados.

## 🧪 Alinhamento e comparação de proteínas:

Foi utilizado o PairwiseAligner, disponível no Biopython, para realizar alinhamentos globais entre:

HBB × HBA1
HBB × VHL
HBA1 × VHL

A identidade foi calculada como:

identidade =
posições idênticas / posições alinhadas × 100

A cobertura foi calculada separadamente para cada sequência:

cobertura =
posições alinhadas / comprimento da sequência × 100

Resultados
Comparação	Identidade	Cobertura 1	Cobertura 2
HBB × HBA1	53,03%	89,80%	92,96%
HBB × VHL	52,63%	77,55%	53,52%
HBA1 × VHL	47,50%	84,51%	56,34%

Observação: os valores representam os resultados obtidos sob os parâmetros definidos no projeto. A identidade obtida por alinhamento global não deve ser interpretada isoladamente como evidência de homologia evolutiva.

## 🧠 Competências demonstradas:
Este projeto permitiu desenvolver e aplicar competências relacionadas a:

1. manipulação de sequências biológicas;
2. leitura e processamento de arquivos FASTA e GenBank;
3. identificação de regiões codificantes (CDS);
4. tradução de sequências nucleotídicas em proteínas;
5. caracterização físico-química de proteínas;
6. organização e análise de dados em CSV;
7. alinhamento global de sequências proteicas;
8. cálculo de identidade e cobertura;
9. visualização de dados moleculares com Matplotlib;
10. desenvolvimento de scripts em Python;
11. organização de pipelines computacionais;
12. reprodutibilidade e versionamento com Git e GitHub.

## 🗂️ Estrutura do projeto:

projeto_01_genomica_bioinformatica/
│
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
├── resultados/
│   ├── perfil_molecular.csv
│   ├── perfil_molecular_final.csv
│   └── figuras/
│       ├── comprimento_proteinas.png
│       ├── peso_molecular.png
│       ├── ponto_isoeletrico.png
│       └── gravy.png
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
│   ├── 09_validar_homologia.py
│   └── 10_visualizar_resultados.py
│
├── validacao/
│   └── validacao_final.txt
│
├── .gitignore
├── README.md
└── requirements.txt

## 💻 Tecnologias utilizadas:
Python 3.13
Biopython 1.88
NumPy 2.5.1
Matplotlib 3.11.1
CSV
PairwiseAligner
PowerShell
Git
GitHub

## ⚙️ Como reproduzir o projeto:

1. Clonar o repositório
git clone https://github.com/marciaoliveira-bio/projeto-01-genomica-bioinformatica.git

2. Entrar na pasta
cd projeto-01-genomica-bioinformatica

3. Criar o ambiente virtual
python -m venv .venv

4. Ativar o ambiente virtual
No Windows PowerShell:
.\.venv\Scripts\Activate.ps1

5. Instalar as dependências
pip install -r requirements.txt

6. Executar as análises

Os scripts estão organizados sequencialmente na pasta scripts/.

Exemplo:

python scripts\01_buscar_hbb.py

Para gerar as visualizações:

python scripts\10_visualizar_resultados.py

Saída esperada:

Visualizações refinadas com sucesso.
Arquivos salvos em:
resultados\figuras

## 🔁 Reprodutibilidade:

O projeto foi organizado de forma a separar:

Dados
  ↓
Processamento
  ↓
Análise
  ↓
Resultados
  ↓
Visualização

Essa organização facilita a rastreabilidade dos dados, a reprodução das análises e a expansão futura do pipeline.

## 🚀 Próximos passos:

Este projeto representa uma primeira etapa prática na construção de um portfólio em Bioinformática e Genômica.

Possíveis extensões incluem:

a) análise de novas sequências;
b) utilização de bancos de dados biológicos;
c) automação de consultas;
d) análise de variantes;
e) alinhamentos múltiplos;
f) análise de expressão gênica;
g) introdução a dados de NGS;
h) desenvolvimento de pipelines mais complexos;
i) integração com ferramentas de bioinformática de linha de comando.

## 👩‍🔬 Autora:
Márcia Oliveira
Biomedicina | Genética e Biologia Molecular | Bioinformática

Projeto desenvolvido como parte da construção de um portfólio prático e do desenvolvimento de competências em análise computacional aplicada às Ciências Biomédicas.
