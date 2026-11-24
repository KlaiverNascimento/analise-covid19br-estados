# analise-covid19br-estados

Projeto de análise de dados focado na evolução de casos e na taxa de mortalidade por COVID-19 nos estados brasileiros (2020–2023), utilizando **Python (Pandas/NumPy)**, **SQLite** e **Matplotlib** a partir de arquivos locais (sem dependência de APIs externas).

Além da prática técnica de limpeza, modelagem relacional e visualização de dados, o estudo busca preservar a memória do impacto humano e social desse período por meio de registros públicos e transparência analítica.

## Fonte dos Dados

Os dados históricos por estado são provenientes do repositório público mantido por Wesley Cota: [wcota/covid19br](https://github.com/wcota/covid19br).

## Estrutura e Fluxo do Projeto

O fluxo está sendo organizado de forma modular para separar tratamento, armazenamento/regras em SQL e visualização:

- **Fonte de dados (`fontes/`):** Armazena o arquivo CSV bruto original, mantido intacto para garantir rastreabilidade e reprodutibilidade.
- **Funções de cálculo (`funcoes/` ou `src/`):** Contém o módulo com a função `porcentagem_regional`, responsável por calcular percentuais com proteção contra divisão por zero e arredondamento de casas decimais.
- **Tratamento e carga (Notebook):** Seleciona as colunas relevantes, aplica a padronização de nomenclatura com prefixos (`DAT_`, `NME_`, `NUM_`), remove agregações totais (`TOTAL`) misturadas à coluna de estados para evitar dupla contagem, realiza validações estatísticas (como checagem de valores negativos oriundos de revisões retroativas) e grava a base limpa na camada **ODS** do SQLite.
- **Modelagem e regras no banco (SQLite):** Armazena os dados tratados localmente e permite aplicar regras analíticas via *Views* (como marcação de *flag* e piso em zero para ajustes negativos, além de consultas consolidadas por estado e período).
- **Visualização (Matplotlib):** Etapa seguinte para consumir os dados já tratados e estruturados e gerar os gráficos analíticos.

## Próximos Passos

- Finalizar a carga da tabela tratada no SQLite (camada ODS).
- Criar as *Views* e consultas SQL para consolidar métricas (como letalidade e participações percentuais).
- Desenvolver os gráficos no Matplotlib e documentar os principais achados da análise.