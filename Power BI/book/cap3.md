#  🪧 **CAP.3 - POWER BI**
## **Dashboard e Storytelling com Power BI**
### **Processo de design de relatório**
Com uma ferramenta como o Power BI, há infinitas possibilidades de como visualizar nossos dados. Felizmente, muitos analistas de dados peneiraram os dados e chegaram a algumas práticas recomendadas, então agora temos um caminho claro para fazer isso.

#### **Por onde eu começo?**
Podemos começar a definir nossa história respondendo a quatro perguntas-chave. Se não pudermos responder a essas perguntas, não devemos prosseguir com a implementação de um painel completo. Em vez disso, devemos retornar à nossa análise exploratória de dados para determinar as respostas.

**1. Qual é meu objetivo?**

Primeiro, precisamos definir o objetivo concreto para a análise. Isso nos ajuda a enquadrar qual é o propósito principal da análise e definir a direção para o resto do projeto. Alguns exemplos disso podem ser:

- Maximizar o lucro
- Reduzir o Custo dos Produtos Vendidos (CPV)

**2. Para quem será essa história?**

Depois de definirmos o objetivo de alto nível para a análise, precisamos decidir o que e como os usuários consumirão a análise. Isso é muito importante porque, com base na resposta, várias versões podem ser necessárias para atingir o objetivo final. Um exemplo dessa diferença é entre o CFO e o Store Director.

O CFO está interessado nas seguintes métricas:

- Tendências trimestrais das margens de lucro
- Repartição trimestral dos custos
- Categorias com melhor e pior desempenho

Enquanto isso, o Diretor da Loja está interessado em outro conjunto de X:

- Repartição mensal de custos e vendas
- Produtos com melhor e pior desempenho
- Contas a receber semanais do cliente

Como podemos ver, embora os interesses possam ser semelhantes, eles são de fato diferentes, o que pode mudar a forma como as informações são apresentadas. Isso ocorre porque o CFO se importa com os KPIs de nível mais alto que impulsionam o negócio, enquanto o Diretor da Loja se importa em como implementar o feedback da equipe executiva. Muito interessante que duas pessoas possam ter visões tão diferentes sobre os dados, certo?

**3. Que ações os usuários podem tomar a partir desses insights?**

A melhor prática para qualquer análise é garantir que os usuários finais possam agir após revisar a análise. Uma vez que sabemos o objetivo e quem serão os usuários finais, podemos começar a definir isso. Eles podem ser organizados em uma lista de itens de ação/decisão orientados por dados, também às vezes chamados de “Fila de Trabalho” ou “Lista de Tarefas”.

No caso do cenário com o CFO e o Diretor de Loja, algumas potenciais Listas de Tarefas poderiam ser:

- Lista dos produtos mais vendidos com margens de lucro
- Lista de clientes que apresentaram diminuição na atividade de compra

**4. Com que frequência preciso atualizar os dados?**

Uma das últimas perguntas que precisamos responder antes de começar nossa análise é com que frequência precisamos atualizar os dados. Isso depende dos 3 fatores anteriores que já respondemos.

### **Melhores práticas de narrativa de dados (princípios da Gestalt)**
Existem sete princípios que precisamos seguir ao projetar histórias de dados, independentemente da ferramenta. Com base em pesquisas de psicologia em percepção visual, eles nos ajudam a dar sentido e organizar informações visuais complexas. Eles também nos ajudam a tornar a narrativa de dados divertida! Eles são conhecidos como Princípios da Gestalt. São os seguintes:

- Enclosure / Figure-Ground : Um enclosure é um grupo de objetos colocados juntos com um limite ao redor deles. Essa técnica é usada na visualização de dados colocando uma borda, sombra ou caixa ao redor de widgets semelhantes que gostaríamos que o usuário revisasse ao mesmo tempo. Isso é especialmente útil ao adicionar KPIs ao painel, criando uma área delineada específica para que o usuário saiba que os KPIs devem ser visualizados juntos.
- Similaridade : Similaridade é quando temos pontos de dados com atributos semelhantes, como cor, direção ou forma. Quando isso acontece, percebe-se que eles são parte de um grupo. Por exemplo, se estivermos visualizando departamentos, podemos querer usar cores para cada departamento, além de anexos, para tornar os diferentes departamentos facilmente distinguíveis uns dos outros.
- Fechamento : Nossos olhos adicionam quaisquer elementos faltantes a formas familiares. Um exemplo disso é não precisar de um fechamento em torno de um gráfico de barras, porque temos um eixo X e um Y para nos ajudar a entender onde estão os limites do gráfico.
- Continuidade : Este princípio tem a ver com a direção em que lemos a história. A ordem em que colocamos as visualizações pode influenciar como o usuário lê os dados.
- Conexão : Temos a tendência de perceber objetos que estão conectados de alguma forma como parte do mesmo grupo ou tema. Isso pode ser uma conexão usando uma seta para mostrar etapas em um processo, por exemplo.
- Proximidade : Este princípio é quando colocamos objetos que são semelhantes próximos uns dos outros. Diferente de Similaridade, este princípio se refere ao arranjo de objetos. Um exemplo disso é colocar todos os widgets juntos, o que pode ser uma visão ligeiramente diferente dos mesmos dados para que o usuário possa ver que eles estão relacionados.
- Simetria : Simetria é o conceito que afirma que elementos que estão muito distantes podem ser percebidos como relacionados, desde que sejam colocados simetricamente no relatório ou painel. Ter objetos colocados simetricamente agrada aos visualizadores e faz com que o relatório ou painel pareça harmonioso.

### **Estrutura do Relatório**
Ao criar um relatório a partir de algumas visualizações, queremos ter certeza de que temos alguns elementos-chave delineados no painel claramente. Esses itens são os seguintes:

- KPIs
- Visualizações / Gráficos dos KPIs
- Dados brutos / Lista de itens de ação

Eles podem ser organizados de várias maneiras. O Salesforce tem alguns layouts de melhores práticas que descrevem como projetar dashboards para aproveitar ao máximo o espaço e causar o maior impacto ao usuário.

#### **Padrão F**
![padraof](https://static-assets.codecademy.com/Courses/bi-dashboards-tableau/storytelling-03.png?_gl=1*1j3835b*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4Mzk5MzguNTguMC4w)

No padrão F, os filtros são mostrados na parte superior do painel para ajudar a dar aos usuários o controle para criar subconjuntos dos dados. Os KPIs são mostrados no lado esquerdo do painel, seguidos por algumas visualizações à direita, criando os dois traços da letra F. À direita disso, há detalhes adicionais que destacam ainda mais quaisquer insights. Por fim, na parte inferior, estão as ações que precisam ser tomadas a partir do painel.

#### **Padrão Z**
![padraoz](https://static-assets.codecademy.com/Courses/bi-dashboards-tableau/storytelling-04.png?_gl=1*1j3835b*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4Mzk5MzguNTguMC4w)

Além do padrão F, o padrão Z é um dos designs mais comuns de dashboards que normalmente é criado. No design Z, os KPIs são colocados na seção Resumo da página. Abaixo dos KPIs estão uma ou duas visualizações que resumem os KPIs junto com informações adicionais sobre eles. Na parte inferior está a lista acionável, geralmente algum tipo de tabela de dados brutos. Esse padrão é chamado de padrão Z porque o olho lê da esquerda para a direita, depois para baixo até as visualizações, depois da esquerda para a direita novamente nos itens de ação.

#### **Padrão lado a lado**
O padrão lado a lado inclui duas visualizações uma ao lado da outra na mesma linha

![padraoladoalado](https://static-assets.codecademy.com/Courses/bi-dashboards-tableau/storytelling-05.png?_gl=1*19mhops*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4Mzk5MzguNTguMC4w)

O último layout comum é o layout Lado a Lado. Neste layout, há algumas visualizações que estão bem próximas uma da outra com uma lista acionável na parte inferior. Esta visualização pode ter KPIs no topo da página, mas se tiver KPIs que não se relacionam diretamente com os gráficos, pode se transformar no padrão Z. Este padrão é melhor usado ao comparar várias métricas usando agrupamentos semelhantes, como tempo ou categorias.

### **Filtros**
Antes de criar filtros, precisamos fazer algumas perguntas. Precisamos nos perguntar o que queremos que os filtros façam e determinar que tipos de filtros queremos adicionar. Se não considerarmos primeiro os usuários finais que estarão interagindo com o painel, criaremos algo que não é tão eficaz quanto gostaríamos.

Por exemplo, se uma categoria já estiver exibida no painel, ela não deve estar no painel de filtros. O motivo para isso é porque ter muitos filtros pode ocupar espaço valioso na tela, o que distrai o visualizador do conteúdo. Além disso, os filtros devem ser intuitivos, pois o usuário sabe exatamente para que são usados. Aqui estão algumas coisas adicionais a serem consideradas:

- Tente aplicar filtros a cada widget no painel
- Organize os filtros em ordem com a maior importância no topo
-Ocultar filtros que não agregam valor ao painel (fadiga do filtro)

Existem três tipos de filtros no Power BI. São eles:
![filtro](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/storytelling/05-filter-types.png?_gl=1*r3dsvy*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4Mzk5MzguNTguMC4w)

- Filtros de visualização : podemos adicionar filtros a um visual que são mostrados na visualização ou pontos de dados adicionais no conjunto de dados. Os campos que são usados ​​na visualização são automaticamente nesta seção com "Todos" selecionado. Campos adicionais podem ser puxados para a seção "Filtros neste visual" arrastando-os da área Campos. Isso é normalmente usado quando queremos focar uma visualização em um subconjunto específico dos dados, como um KPI que queremos rastrear para um grupo específico de dados.
- Filtros de página : Os filtros de página são adicionados arrastando campos para a seção “Filtros nesta página”. Esses são os mais comuns e podem ser colocados diretamente na página. Eles são ótimos para permitir que os usuários finais consigam manipular os dados sem precisar de assistência para manipulá-los.
- Filtros de Relatório : Os filtros de relatório são adicionados à seção “Filtros em todas as páginas”. Esta seção filtrará os dados do conjunto de dados, não importa em qual página o usuário esteja. Esta é uma opção alternativa, em vez de filtrar no nível do Power Query.
- Visualizações de Slicer : Um slicer é uma visualização que puxa um filtro diretamente para o painel. Eles funcionam estritamente como filtros de página. É outra maneira de garantir que pontos de dados específicos sejam alternados. Eles funcionam especialmente com datas ou qualquer intervalo de números em que um controle deslizante é preferível a uma lista suspensa.

### **Estrutura do painel do Power BI**
Depois que tivermos um relatório criado com várias páginas, devemos começar a explorar o painel usando nossas visualizações que adicionamos a cada relatório. Podemos adicionar quantas visualizações quisermos ao painel das diferentes páginas do relatório.

![estruturapainelbi](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/storytelling/06-power-bi-dashboard.gif?_gl=1*15qdpjm*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4Mzk5MzguNTguMC4w)

Os painéis do Power BI nos permitem criar visualizações específicas de dados que queremos destacar para os usuários finais. O Power BI nos permite interagir com os dados no painel, mas o principal caso de uso é destacar visualizações interessantes específicas, como métricas e tendências. Ainda podemos nos aprofundar mais e interagir com o relatório de onde a visualização veio simplesmente clicando no bloco do painel. Sem mencionar que eles são muito legais e podemos organizá-los rapidamente como quisermos!

### **Refinamento da história de dados**
Depois que tivermos nosso painel e história criados, podemos começar a refinar nossa história de dados. É importante que nossos dados sejam fáceis de interpretar e tenham significado. Podemos aprimorar nossa história de dados refinando nossas páginas e painéis usando algumas das técnicas abaixo.

#### **Refinamento de gráfico**
Depois que tivermos nossos gráficos criados, eles provavelmente precisarão de algum refinamento. Aqui estão algumas dicas para os diferentes tipos de gráficos que devemos ter em mente:

**Gráficos de comparação**

- Sempre classifique as categorias em ordem crescente ou decrescente
- Garantir que o eixo esteja sempre ancorado em zero
- Use uma cor para cada medida, nunca uma cor por categoria

**Gráficos de tendências**

- Nunca mostre mais de 4 linhas em um gráfico de tendências
- Use um eixo duplo para mostrar unidades semelhantes que têm escalas muito diferentes

**Gráficos de relacionamento**

- Comece sempre do zero para ambos os eixos
- Use cores para destacar valores discrepantes e padrões

#### **Em todos os tipos de gráficos**

- Mostrar comparações : garanta que haja contexto ao comparar vários itens, especialmente ao mostrá-los ao longo do tempo
- Mostrar Causalidade : Garanta que, se uma correlação entre medidas estiver presente, esse insight seja apresentado aos usuários finais. Isso também pode ser mostrado em um eixo duplo, com a mesma dimensão de tempo.
- Use Dados Multivariados : Use tantas categorias relacionadas quanto fizer sentido. Alavancar cor, tamanho, forma e posição pode impactar significativamente a qualidade da história.
- Modos de integração completos : garanta que, sempre que possível, texto, números e até imagens sejam incluídos nas visualizações.

### **Dicas de ferramentas**
Dicas de ferramentas são as caixas de texto que aparecem ao passar o mouse sobre um gráfico. Elas fornecem informações que podem ou não ser visíveis para os usuários no gráfico. Essas caixas de texto podem ser personalizadas para que forneçam as informações mais úteis rapidamente para os usuários. O Power BI tem algumas etapas para fazer isso:

1. Comece com uma dica de ferramenta básica e extraia informações importantes para a seção Dicas de ferramentas da visualização.
2. Identifique o item mais importante da lista e ordene-o no topo da dica de ferramenta
3. Adicione agregações adicionais à dica de ferramenta arrastando campos para a seção Dicas de ferramenta e alterando o tipo de agregação

![dicasferramentas1](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/storytelling/07-custom-tooltip.png?_gl=1*do5qmb*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4Mzk5MzguNTguMC4w)

Além disso, podemos adicionar páginas como dicas de ferramentas para dar muitas informações extras além do texto básico que uma dica de ferramenta típica oferece. Para fazer isso, siga estas etapas:

1. Crie uma nova página e altere o tamanho da página para “Dica de ferramenta”
2.Adicionar uma visualização à página
3. Vá para Formatar > Informações da página e ative a Dica de ferramenta
4. Volte para a primeira página, clique na visualização
5. Vá em Formatar > Dica de ferramenta > Tipo e selecione a página que acabamos de criar
6. Agora, quando passarmos o mouse sobre o gráfico, veremos a dica de ferramenta que acabamos de criar

![dicasferramentas2](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/storytelling/08-page-tooltip.png)