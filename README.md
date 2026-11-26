# analise-covid19br-estados

Projeto de análise de dados focado na evolução de casos e na taxa de mortalidade por COVID-19 nos estados brasileiros (2020–2023), utilizando **Python (Pandas/NumPy)**, **SQLite** e **Matplotlib** a partir de arquivos locais (sem dependência de APIs externas).

Além da prática técnica de limpeza, modelagem relacional e visualização de dados, o estudo busca preservar a memória do impacto humano e social desse período por meio de registros públicos e transparência analítica.

## Fonte dos Dados

Os dados históricos por estado são provenientes do repositório público mantido por Wesley Cota: [wcota/covid19br](https://github.com/wcota/covid19br).

## Tecnologias

- **Python 3** com **Pandas** e **NumPy** para leitura, limpeza e cálculos.
- **SQLite** (via `sqlite3` e `pandas.to_sql`) para armazenamento local da camada ODS.
- **Matplotlib** para a visualização dos resultados (etapa em andamento).
- **Jupyter Notebook** para o fluxo de tratamento de dados.

## Estrutura e Fluxo do Projeto

O fluxo está sendo organizado de forma modular para separar tratamento, armazenamento/regras em SQL e visualização:

```
analise-covid19br-estados/
├── fontes/                       # CSV bruto (cases-brazil-states.csv)
├── funçoes/
│   └── calculos.py               # Função porcentagem_regional
├── projeto-principal/
│   └── 01_tratamento_dados.ipynb # Tratamento e carga no SQLite
├── database/
│   └── covid19br.db              # Banco SQLite (tabela ODS_COVID_ESTADOS)
└── sql/
    └── consultas-sql.sql         # Consultas e Views (em construção)
```

- **Fonte de dados (`fontes/`):** Armazena o arquivo CSV bruto original, mantido intacto para garantir rastreabilidade e reprodutibilidade.
- **Funções de cálculo (`funçoes/`):** Contém o módulo com a função `porcentagem_regional`, que calcula percentuais, aplica a regra `total > 0` para evitar divisão por zero e arredonda o resultado para a quantidade de casas decimais informada (padrão: 2).
- **Tratamento e carga (Notebook):** Seleciona as colunas relevantes, aplica a padronização de nomenclatura com prefixos (`DAT_`, `NME_`, `NUM_`), remove a linha agregada `TOTAL` misturada à coluna de estados para evitar dupla contagem, faz uma primeira inspeção estatística com `describe()` nas colunas de óbitos e grava a base limpa na camada **ODS** do SQLite.
- **Modelagem e regras no banco (SQLite):** Armazena os dados tratados localmente e, como planejado, aplicará regras analíticas via *Views* (marcação de *flag* e piso em zero para ajustes negativos, além de consultas consolidadas por estado e período).
- **Visualização (Matplotlib):** Etapa seguinte para consumir os dados já tratados e estruturados e gerar os gráficos analíticos.

## Modelo de Dados (Camada ODS)

A tabela `ODS_COVID_ESTADOS`, no arquivo `database/covid19br.db`, contém os registros diários por estado, já tratados:

| Coluna | Tipo | Origem no CSV | Descrição |
| --- | --- | --- | --- |
| `DAT_OCORRIDO` | TEXT | `date` | Data do registro (`AAAA-MM-DD`) |
| `NME_REGIAO_OCORRIDO` | TEXT | `country` | Região/país do registro |
| `NME_ESTADO_OCORRIDO` | TEXT | `state` | Sigla do estado |
| `NUM_NOVO_OBITO` | INTEGER | `newDeaths` | Óbitos novos no dia |
| `NUM_OBITO` | INTEGER | `deaths` | Óbitos acumulados |
| `NUM_NOVOS_CASOS` | INTEGER | `newCases` | Casos novos no dia |
| `NUM_TOTAL_CASOS` | INTEGER | `totalCases` | Casos acumulados |
| `NUM_OBITOS_100K_HABITANTES` | REAL | `deaths_per_100k_inhabitants` | Óbitos acumulados por 100 mil habitantes |

Na carga atual, a tabela possui **29.724 linhas**, **27 estados/unidades** distintos e período de **25/02/2020 a 18/03/2023**.

## Como Executar

1. Instale as dependências: `pip install pandas numpy matplotlib`.
2. Abra `projeto-principal/01_tratamento_dados.ipynb` a partir da pasta `projeto-principal/` (os caminhos são relativos, como `../fontes/` e `../database/`).
3. Execute as células em ordem. O notebook regrava a tabela `ODS_COVID_ESTADOS` a cada execução (`if_exists="replace"`).

## Status Atual

- [x] Seleção e renomeação das colunas com padrão de prefixos.
- [x] Remoção da linha agregada `TOTAL`.
- [x] Carga da camada ODS no SQLite (`ODS_COVID_ESTADOS`).
- [ ] Validação de valores negativos oriundos de revisões retroativas.
- [ ] Views e consultas SQL em `sql/consultas-sql.sql` (arquivo ainda vazio).

## Próximos Passos

- Implementar a checagem de valores negativos e decidir a regra de tratamento (ex.: piso em zero com *flag*).
- Criar as *Views* e consultas SQL para consolidar métricas (como letalidade e participações percentuais).
- Desenvolver os gráficos no Matplotlib e documentar os principais achados da análise.