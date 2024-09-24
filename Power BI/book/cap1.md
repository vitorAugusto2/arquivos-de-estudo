#  🪧 **CAP.1 - POWER BI**
## **Introdução aos painéis de BI com o Power BI**
### **O que é Power BI ?**
Power BI é uma ferramenta de visualização e análise de dados desenvolvida pela Microsoft. Ela permite conectar diversas fontes de dados, criar relatórios interativos e dashboards personalizados, e compartilhar essas análises com outros usuários, facilitando a tomada de decisões baseados em dados.

### **Instalação**
Vamos começar a instalar o Power BI.  [Aqui está a página de download.](https://www.microsoft.com/en-us/download/details.aspx?id=58494) Depois de baixar o Power BI, você pode [criar um perfil](https://community.fabric.microsoft.com/t5/Data-Stories-Gallery/bd-p/DataStoriesGallery) e selecionar “Registrar” na parte superior da página.

**Nota:** para fazer upload de projetos para a nuvem e compartilhar com sua organização, precisará ter uma conta organizacional com a Microsoft. Se desejar, você pode [fazer upload para a galeria da comunidade.](https://community.fabric.microsoft.com/t5/Power-BI-forums/ct-p/powerbi).

## **Carregando e trabalhando com dados no Power BI**
### **Carregando dados**
Primeiramente, precisamos ter certeza qual fonte de dados queremos nos conectar antes de tentar carregar no Power BI e se é suportada. [Aqui está uma lista de fontes de dados que o Power BI suporta](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-sources).

Para carregar o arquivo no Power BI:
- Primeiro vá em “Obter dados”
- Em seguida, selecione “Texto/CSV”
- Selecione o arquivo e depois “Abrir”

![Carregar arquivo](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/load-file-02.gif?_gl=1*1t6z18y*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4wLjE3MjE3NTU1ODIuMjUuMC4w)

#### **Conectando-se a bancos de dados e fontes on-line**
O segundo tipo de fonte de dados são os dados do servidor, que você pode acessar conectando-se a um servidor. Alguns exemplos de fontes de dados do servidor incluem Microsoft SQL Server, Azure SQL, Google Sheets e Snowflake. As fontes de dados do servidor são uma ótima maneira de trabalharmos com conjuntos de dados que são muito grandes para armazenarmos em nossa máquina local/no local. Usar uma conexão de servidor nos permite atualizar os dados com mais frequência sem precisar atualizar manualmente nenhum arquivo estático.

Ao selecionar um arquivo, uma janela aparecerá para selecionar o arquivo. Ao selecionar um servidor, seremos solicitados a fornecer nossas credenciais/autenticação do servidor. Depois de selecionar um servidor e inserir todas as credenciais, passaremos para a tela “Data Source”.

No Power BI, muitos tipos diferentes de fontes de dados podem ser combinados. Arquivos planos (Excel, CSV) e fontes de servidor podem ser transformados e unidos para gerar insights interessantes a partir dos dados.

#### **Transformar Dados**
Depois que a fonte de dados for selecionada, temos a opção de Transformar os dados. Significa que podemos alterar e manipular qualquer coisa sobre o conjunto de dados antes que ele seja carregado no Power BI. Alguns exemplos disso são:
- Filtrando Colunas
- Removendo / Adicionando colunas
- Alterar tipos de dados
- Dividir colunas
- Dados de grupo (semelhantes a tabelas dinâmicas)
- Junte dados
- Escreva fórmulas personalizadas (DAX)

![Transformar Dados](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/transform-data-prompt-03.png?_gl=1*nhxth3*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4wLjE3MjE3NTU1ODIuMjUuMC4w)

Após selecionar o botão “Transform Data”, somos levados a uma tela com o título “Power Query Editor”. Esta tela é onde faremos quaisquer ajustes no conjunto de dados antes de transformar e modificar nossos dados para que possamos gerar visualizações interessantes a partir deles.

![Power Query Editor](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/transform-data-screen-04.png?_gl=1*1vleep2*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4wLjE3MjE3NTU1ODIuMjUuMC4w)

**Nota:** Podemos usar *Joins* para conjuntos de dados que precisamos analisar, provavelmente precisaremos juntá-los para dar sentido aos dados, como: *Merge*, *Left Join*, *Inner Join* ...

#### **Trabalhando com dados no Power BI**
Depois que nossos dados forem carregados no Power BI, podemos começar a trabalhar com eles no Power Query Editor. Isso nos permitirá refinar o conjunto de dados e limpá-lo antes de ser usado para painéis. Uma das muitas coisas boas (e há muitas!) sobre o Power Query Editor é que podemos rastrear as etapas individuais que foram tomadas para modificar o conjunto de dados dentro do editor. Isso significa que sempre teremos um log de auditoria do que foi alterado e como foi alterado se quisermos voltar e fazer atualizações.

#### **Tipos de dados**
Ao carregar dados no Power BI, a primeira tarefa que precisa ser concluída é verificar se os tipos de dados estão corretos. Tipos de dados incorretos causarão problemas quando chegarmos ao nível do painel.

No exemplo do conjunto de dados Hotel Booking Demand, o campo “agent” carrega como um campo de texto em vez de numérico. Para alterar isso, selecionamos o ícone “ABC” no topo da coluna e o alteramos para “123 Whole Number”.

![Tipo de dados](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/data-type-example-10.png?_gl=1*flce3c*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4wLjE3MjE3NTU1ODIuMjUuMC4w)

#### **Ferramenta do Editor de Power Query**
O [Power Query](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query) é um mecanismo de transformação e preparação de dados que permite aos usuários modificar dados antes que eles cheguem ao Power BI. O Power Query pode ser usado tanto no Excel quanto no Power BI. É um dos recursos mais poderosos do Power BI. Ele nos permite pegar dados que podem ser um pouco estruturados e nos permite manipular e modificar esses dados para que se ajustem ao formato que queremos para fins de visualização de dados.

O Power Query nos permite fazer muitas coisas, mas as ações mais comuns são:
- Substituir dados
- Classificar dados
- Dados de grupo e pivô
- Criação de perfil de dados (visualizar distribuição de campos e qualidade de dados)

![Power Query](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/what-is-power-query-11.png?_gl=1*zoqt7a*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4wLjE3MjE3NTU1ODIuMjUuMC4w)

#### **Substituir dados**
O primeiro passo para limpar nossos dados é substituir valores que não queremos em nosso conjunto de dados. Isso pode ser algo tão simples quanto substituir NULLs por outro valor, eliminando valores duplicados, ou tão complexo quanto substituir valores em uma coluna por nomes.

A funcionalidade de substituição realmente nos permite garantir que os dados apresentados sejam exatamente o que os usuários finais esperariam. Por exemplo, vamos imaginar que para o conjunto de dados Hotel Booking Demand queremos pegar todos os NULLvalores na coluna “Agent” e substituí-los por 0. Podemos fazer isso da seguinte maneira:
- Selecione a coluna e depois “Substituir Valores” no cabeçalho.
- No pop-up “Substituir valores”, insira os valores que queremos encontrar e os valores pelos quais queremos substituí-los.

![Susbitituir dados](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/replace-data-12.gif?_gl=1*b1d00m*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4xLjE3MjE3NTcxNTUuNjAuMC4w)

#### **Classificar dados**
Classificar dados também ajuda na preparação de dados e nos ajuda a identificar erros. Podemos escolher classificar por uma única coluna ou até mesmo por várias colunas. Para fazer isso, identificamos as colunas pelas quais queremos classificar e as selecionamos em ordem de importância.

No caso do conjunto de dados Hotel Booking Demand, classificaremos 'deposit_type' em ordem decrescente e depois 'days_in_waiting_list'em ordem decrescente. Isso nos dirá se há outliers e transações que estavam fora da janela aceita.

![Classificar dados](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/sort-data-example-13.png?_gl=1*zrosef*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4xLjE3MjE3NTcxNTUuNjAuMC4w)

#### **Dados do grupo**
Agrupar dados nos permite consolidar os dados em um formato mais consumível. Podemos fazer isso selecionando a coluna pela qual gostaríamos de agrupar e, em seguida, selecionando “Agrupar por” no topo da página. Em seguida, veremos um modal aparecer com opções básicas e avançadas. A diferença entre as duas é que a opção básica nos permitirá usar uma coluna e uma agregação, enquanto a opção avançada nos permitirá adicionar várias colunas de agrupamento e várias agregações.

No caso do conjunto de dados de Demanda de Reservas de Hotéis, podemos agrupar nossos dados fazendo o seguinte:
- Selecione a consulta no lado esquerdo e duplique-a. Isso nos permitirá criar um agrupamento sem perturbar os dados brutos.
- Em seguida, selecionaremos a hotelcoluna e, em seguida, selecionaremos “Agrupar por”.
- Agora selecionaremos “Avançado” porque queremos agregar por múltiplas colunas.
- Selecionaremos “hotel” como primeiro agrupamento e depois is_cancelledcomo segunda opção.
- Quanto à agregação, deixaremos isso como Contagem e Contagem de Linhas.
- Após inserir, selecione “OK”.

![Dados do grupo](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/group-data-14.gif?_gl=1*1dy9vtq*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4xLjE3MjE3NTcxNTUuNjAuMC4w)

### **DAX (Expressões de Análise de Dados)**
O Power Query também nos permite criar expressões personalizadas para atender às nossas necessidades. Não importa qual modificação personalizada queremos fazer nos dados, quase sempre há uma maneira de fazer isso. Este é um dos principais diferenciais entre o Power BI e outras ferramentas de BI. Existem três agrupamentos básicos para fazer isso:

- Funções lógicas (if/else)
- Funções de agregação (soma, máximo, média, etc.)
- Funções matemáticas (aleatório, arredondamento, valor absoluto)

#### Funções lógicas
Funções lógicas são semelhantes a IFinstruções no Excel. Isso nos permite criar agrupamentos personalizados que atendem melhor às nossas necessidades conforme analisamos os dados. Por exemplo, no conjunto de dados Hotel Booking Demand, queremos categorizar o “lead_time” em dois buckets:
- Mais de 150 dias
- Menos de 150 dias

A maneira como faremos isso é:
- Vá em “Adicionar coluna” no topo da página e selecione “Coluna condicional”.
- Nomeie esta coluna como “Grupo de Prazo de Entrega”.
- Em Nome da coluna, selecione lead_time, depois “é maior ou igual a” e depois 150. Isso agora nos permitirá nomear nossos buckets nos campos Saída e Senão restantes.
- Depois de preenchido, selecione “OK” e a nova coluna deverá aparecer no final do conjunto de dados.

![Funcoes logicas](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/logical-function-15.png?_gl=1*bv5imy*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4xLjE3MjE3NTcxNTUuNjAuMC4w)
 
#### Funções de agregação
Existem alguns tipos diferentes de agregações disponíveis no Power BI. São eles:
- Soma
- Média
- Mediana
- Mínimo
- Máx.
- Contagem de linhas
- Contar linhas distintas

Voltando ao Grouping data, vimos que havia diferentes operações que poderíamos aplicar aos dados. Legal! Ao agrupar dados, podemos começar a analisar dados para ter uma noção melhor de como o conjunto de dados se parece, bem como criar algumas métricas personalizadas para nós mesmos.

Para o conjunto de dados de Demanda de Reservas de Hotéis, fazemos o seguinte:
- Selecione nossa consulta duplicada que criamos com o agrupamento.
- No painel direito, passe o mouse sobre a etapa “Grouped Rows” e selecione o ícone de engrenagem. Isso nos levará de volta ao nosso agrupamento e nos mostrará as Operations que estão disponíveis para nós.
- Agora selecionaremos “Adicionar agregação” para adicionar outra agregação à nossa tabela.
- Agora, nomearemos esta nova coluna “Média de dias de lista de espera”, selecionaremos “Média” em Operações e selecionaremos days_in_waiting_listcomo a coluna.
- Uma vez selecionado, selecione “OK” e a nova coluna deverá aparecer.

Observe que para City Hotels, a média de dias na lista de espera é maior para compromissos cancelados do que para compromissos não cancelados. A partir dessa correlação, podemos inferir que quanto mais tempo as pessoas ficam na lista de espera, maior a probabilidade de cancelarem.

![Funcoes agregacao](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/aggregation-function-example-16.png?_gl=1*149r5u3*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4xLjE3MjE3NTcxNTUuNjAuMC4w)

#### Funções matemáticas
Outro tipo de função que podemos fazer é criar funções matemáticas adicionais para nossa consulta. Essas são coisas como:
- Aleatório
- Arredondamento
- Valor absoluto

Essas expressões nos permitem limpar ainda mais os dados e aprimorar a análise que estamos fazendo. Para encontrá-las, vá para “Add Column” no topo da página e vá para a seção “From Number”.

No caso do conjunto de dados de Demanda de Reservas de Hotéis, queremos arredondar a coluna “Avg Days on Waitlist” que acabamos de criar para dar aos usuários uma compreensão mais clara dos números. Para fazer isso:

- Destaque a coluna “Média de dias na lista de espera”.
- Selecione a opção “Arredondamento” no cabeçalho superior.
- Selecione “Round Up”. Isso criará uma nova coluna com os números arredondados para cima.

![Funcoes matematicas](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/round-up-17.gif?_gl=1*1vn17es*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4xLjE3MjE3NTcxNTUuNjAuMC4w)

Para aplicar as alterações do Power Query aos seus dados no Power BI, vá para “Início” na parte superior da página e selecione “Fechar e aplicar”.

![Carregar dados](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/loading-and-working-with-data/close-and-apply-18.png?_gl=1*1j9fl25*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1NTU0Ny4yNC4xLjE3MjE3NTcxNTUuNjAuMC4w)