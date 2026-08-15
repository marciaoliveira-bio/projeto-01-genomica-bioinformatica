# Projeto 01 — Análise Genômica e Bioinformática

**Pipeline introdutório para análise de sequências gênicas e proteicas humanas utilizando Python e Biopython.**

Projeto desenvolvido para aplicar, de forma prática e reprodutível, conceitos de **Biologia Molecular, Genética, análise de sequências e Bioinformática**.

O projeto acompanha um fluxo completo de análise, desde a obtenção de sequências de referência até a caracterização molecular, organização dos resultados e comparação entre proteínas.

---

## 🧬 Visão geral

Neste projeto foram analisados três genes humanos:

| Gene     | Proteína                                      | Contexto biológico                     |
| -------- | --------------------------------------------- | -------------------------------------- |
| **HBB**  | Hemoglobina beta                              | Transporte de oxigênio                 |
| **HBA1** | Hemoglobina alfa 1                            | Transporte de oxigênio                 |
| **VHL**  | Proteína supressora tumoral von Hippel-Lindau | Regulação celular e resposta à hipóxia |

O objetivo foi construir um **pipeline computacional reprodutível** capaz de:

* obter sequências de referência;
* identificar regiões codificantes (CDS);
* traduzir sequências nucleotídicas em proteínas;
* caracterizar propriedades físico-químicas;
* identificar características funcionais;
* organizar resultados em arquivos tabulares;
* realizar comparações entre proteínas;
* calcular identidade e cobertura de alinhamentos.

---

## 🎯 Objetivo

Desenvolver e documentar um fluxo introdutório de análise bioinformática utilizando **Python e Biopython**, integrando conhecimentos de:

* Biologia Molecular;
* Genética;
* Bioinformática;
* análise de sequências;
* análise de proteínas;
* programação em Python;
* organização e interpretação de dados biológicos.

O projeto também foi desenvolvido com foco em **reprodutibilidade computacional**, permitindo que as diferentes etapas sejam executadas novamente a partir dos scripts disponibilizados.

---

## 🔬 Pipeline de análise

O fluxo desenvolvido pode ser resumido da seguinte forma:

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
Organização dos resultados
        ↓
Comparação entre proteínas
        ↓
Alinhamento global
        ↓
Identidade e cobertura
```

---

## 📂 Estrutura do projeto

```text
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
│   └── perfil_molecular_final.csv
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
├── validacao/
│   └── validacao_final.txt
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🧪 Etapas da análise

### 1. Obtenção das sequências

As sequências de referência dos genes selecionados foram obtidas e armazenadas nos formatos **FASTA** e **GenBank**.

Os arquivos GenBank também foram utilizados para acessar informações de anotação, incluindo regiões codificantes.

### 2. Identificação da CDS e tradução

As regiões codificantes (**CDS — Coding DNA Sequence**) foram identificadas e utilizadas para gerar as respectivas sequências proteicas.

O fluxo fundamental foi:

```text
DNA
 ↓
CDS
 ↓
RNA mensageiro
 ↓
Proteína
```

### 3. Caracterização físico-química

As proteínas foram caracterizadas utilizando recursos do Biopython.

Foram analisados:

* comprimento da proteína;
* peso molecular;
* ponto isoelétrico (pI);
* aromaticidade;
* índice de instabilidade;
* GRAVY;
* composição de aminoácidos.

Os resultados foram organizados em arquivos CSV para facilitar a análise e comparação.

### 4. Características funcionais

Foram investigadas características relacionadas às proteínas analisadas.

Para **HBB** e **HBA1**, foram registradas características compatíveis com proteínas da família das globinas.

Para **VHL**, foi registrado o motivo funcional utilizado na análise:

```text
TLKERCLQVV
```

### 5. Organização dos resultados

Os resultados foram estruturados em arquivos CSV.

O arquivo:

```text
resultados/perfil_molecular_final.csv
```

reúne informações moleculares e anotações funcionais obtidas durante o pipeline.

### 6. Validação por alinhamento

Foi utilizado o `PairwiseAligner`, disponível no Biopython, para realizar alinhamentos globais entre:

```text
HBB × HBA1
HBB × VHL
HBA1 × VHL
```

A identidade foi calculada como:

```text
identidade =
posições idênticas / posições alinhadas × 100
```

A cobertura foi calculada separadamente para cada sequência:

```text
cobertura =
posições alinhadas / comprimento da sequência × 100
```

---

## 📊 Resultados principais

Os alinhamentos foram realizados utilizando os seguintes parâmetros:

| Parâmetro           |  Valor |
| ------------------- | -----: |
| Tipo de alinhamento | Global |
| Match score         |      2 |
| Mismatch score      |     -1 |
| Gap opening         |     -2 |
| Gap extension       |   -0.5 |

Resultados obtidos:

| Comparação | Identidade | Cobertura 1 | Cobertura 2 |
| ---------- | ---------: | ----------: | ----------: |
| HBB × HBA1 |     53,03% |      89,80% |      92,96% |
| HBB × VHL  |     52,63% |      77,55% |      53,52% |
| HBA1 × VHL |     47,50% |      84,51% |      56,34% |

**Importante:** esses valores representam os resultados obtidos sob os parâmetros definidos no projeto. Identidade de sequência obtida por alinhamento global não deve ser interpretada isoladamente como evidência de homologia evolutiva.

---

## 💻 Tecnologias utilizadas

* **Python 3.13**
* **Biopython 1.88**
* **CSV**
* **PairwiseAligner**
* **PowerShell**
* **Git**
* **GitHub**

---

## ▶️ Como reproduzir o projeto

Para reproduzir as análises localmente, é necessário ter **Python 3.13** instalado.

### 1. Clonar o repositório

```bash
git clone https://github.com/marciaoliveira-bio/projeto-01-genomica-bioinformatica.git
```

### 2. Entrar na pasta do projeto

```bash
cd projeto-01-genomica-bioinformatica
```

### 3. Criar um ambiente virtual

No Windows PowerShell:

```powershell
python -m venv .venv
```

### 4. Ativar o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 6. Executar os scripts

Os scripts estão organizados na pasta `scripts/` e seguem uma sequência de análise:

```text
01_buscar_hbb.py
02_analisar_hbb.py
03_buscar_alvos.py
04_analisar_alvos.py
05_rastrear_proteinas.py
06_gerar_csv.py
07_motivos_funcionais.py
08_atualizar_csv.py
09_validar_homologia.py
```

Exemplo:

```powershell
python scripts/01_buscar_hbb.py


## 📁 Reprodutibilidade

O projeto foi estruturado para permitir a reprodução das etapas de análise por meio dos scripts disponíveis na pasta:

```text
scripts/
```

A organização separa:

* dados de entrada;
* scripts de análise;
* resultados;
* evidências;
* validações.

Essa estrutura facilita a rastreabilidade entre **dados → processamento → resultados**.

---

## 🧠 Competências demonstradas

Este projeto representa o desenvolvimento prático das seguintes competências:

**Biologia Molecular**

* estrutura e análise de sequências;
* CDS;
* tradução de sequências;
* proteínas.

**Bioinformática**

* manipulação de sequências biológicas;
* análise de proteínas;
* alinhamento de sequências;
* identidade e cobertura.

**Programação**

* Python;
* Biopython;
* manipulação de arquivos;
* estruturas de dados;
* geração e leitura de CSV.

**Organização científica**

* documentação de pipeline;
* organização de dados;
* registro de resultados;
* reprodutibilidade computacional;
* interpretação crítica dos resultados.

---

## ⚠️ Limitações

Este projeto possui caráter **educacional e introdutório**.

Os resultados devem ser interpretados considerando:

* os parâmetros utilizados;
* as características das sequências selecionadas;
* as limitações dos métodos empregados;
* a necessidade de ferramentas complementares para conclusões biológicas mais robustas.

Em particular, os resultados de alinhamento não devem ser utilizados isoladamente para inferir relações evolutivas ou funcionais.

---

## 🚀 Próximos passos

O pipeline será expandido progressivamente para incorporar novas ferramentas e análises de Bioinformática, incluindo:

* análises de similaridade de sequências;
* BLAST;
* análise de variantes;
* anotação funcional;
* análises envolvendo NGS;
* visualização de dados biológicos;
* automação de pipelines;
* integração de diferentes bancos de dados biológicos.

---

## 👩‍🔬 Sobre o projeto

Este repositório faz parte da construção progressiva de competências em **Genética, Biologia Molecular, Bioinformática e programação aplicada às Ciências da Saúde**.

O objetivo é documentar não apenas os resultados finais, mas também a evolução das habilidades técnicas e científicas desenvolvidas ao longo dos projetos.

**Projeto 01 — Análise Genômica e Bioinformática**

**Márcia Oliveira**
