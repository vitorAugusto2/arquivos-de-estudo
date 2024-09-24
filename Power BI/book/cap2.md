#  🪧 **CAP.2 - POWER BI**
## **Visualizações básicas com Power BI**
O Power BI oferece uma variedade de tipos de visualização de dados, então precisamos entender quais opções temos para apresentar a melhor história de dados possível.

![Vizualization](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/visualization-types-01.png?_gl=1*tahdhl*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1OTk4My4yNS4xLjE3MjE3NjAzNjQuNDIuMC4w)

### **Blocos de construção do Power BI**
Como usar os blocos de construção do Power BI — visualizações, relatórios, painéis e aplicativos — para montar nossa análise.

![Blocos de construcao](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/power-bi-diagram-02.png?_gl=1*hn8g4f*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1OTk4My4yNS4xLjE3MjE3NjAzNjQuNDIuMC4w)

#### **Visualizações (Power BI Desktop)**
No Power BI, as páginas também são chamadas de relatórios. Nesta página, podemos criar uma visualização indo para a seção “Visualizações” no lado direito da página e clicando em qualquer uma das visualizações que vemos.

![power BI Desktop](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/visualizations-location-03.png?_gl=1*10186wq*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1OTk4My4yNS4xLjE3MjE3NjAzNjQuNDIuMC4w)

Depois de selecionar o tipo de visualização de nosso interesse, podemos ver algumas seções na tela:
- Página: A página é a tela onde podemos colocar e organizar nossas visualizações.
- Visualizações: Esta seção no lado direito da tela nos permite selecionar entre uma biblioteca de visualizações dentro da ferramenta.
- Campos: Esta seção no lado direito da tela permite que os usuários selecionem campos que foram definidos na etapa de carregamento de dados.
- Configurações de visualização: As configurações de visualização nos permitem adicionar campos ao gráfico para começar a visualizar os dados. - Cada visualização terá configurações ligeiramente diferentes.
- Filtros de Nível Visual: A seção Filters contém tanto Filtros de Nível Visual quanto Filtros de Nível de Página. No caso de visualizações, queremos selecionar a partir dos Filtros de Nível Visual.

![Vizualizations](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/visualization-configuration-04.png?_gl=1*1r1pi0l*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1OTk4My4yNS4xLjE3MjE3NjAzNjQuNDIuMC4w)

#### **Relatórios/Páginas (Power BI Desktop)**
Ao abrir o Power BI, podemos ver as Páginas na parte inferior da tela como guias (semelhante ao Microsoft Excel).

![relatorio1](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/page-05.png?_gl=1*at2gyz*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1OTk4My4yNS4xLjE3MjE3NjAzNjQuNDIuMC4w)

Mas espere — o que é um relatório, afinal? Um relatório é uma coleção de diferentes visualizações, todas em uma única exibição. O ideal seria selecionar várias visualizações que usam a mesma fonte de dados. Isso é útil por alguns motivos:

- Adicionando filtros: Ao adicionar filtros que usam a mesma fonte de dados, os filtros podem ser aplicados a todas as visualizações na página. Isso significa que podemos criar um único filtro na página e ele filtrará todas as visualizações naquela página. Bem legal, certo?
- Cross Filtering: No Power BI, podemos configurar visualizações para que elas possam ser usadas como filtros. O que isso significa é que, uma vez que temos duas ou mais visualizações na página, podemos clicar em uma e ela filtrará as outras.

![relatorio2](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/report-interaction-06.gif?_gl=1*at2gyz*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTc1OTk4My4yNS4xLjE3MjE3NjAzNjQuNDIuMC4w)


#### **Painéis (Power BI Server)**
Os dashboards nos oferecem uma maneira de destacar diferentes insights e facilitar para os usuários finais a leitura da história de dados que reunimos. Semelhante aos relatórios, eles usam visualizações e relatórios como blocos de construção para montar o dashboard.

![Paineis](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/power-bi-new-dashboard-07.png?_gl=1*quzhqz*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4MzkzMTMuMzQuMC4w)

Com dashboards, diferentemente de relatórios/páginas, é considerado uma prática recomendada usar diferentes fontes de dados. Por quê? Aqui, uma variedade de fontes de dados pode ajudar a dar insights sobre o que os dados estão tentando nos dizer. Mais fontes podem nos ajudar a montar uma imagem mais holística do que está acontecendo.

Cada página pode ser anotada para que o usuário final saiba exatamente o que pretendíamos quando criamos a história. Com histórias, podemos criar guias para especificar uma ordem em que queremos revisar os dados e títulos de guias que especificam a área em que queremos que o usuário se concentre. Isso nos permite guiar os usuários por uma análise sem que estejamos presentes.

#### **Aplicativos (Servidor Power BI)**
Um aplicativo no Power BI é uma maneira de criarmos conteúdo empacotado oficial e, então, distribuir aos usuários. Alguns benefícios de criar um aplicativo são:

- Controle de Permissões: Quando criamos um aplicativo, podemos controlar as permissões para o grupo de dados que foi reunido. Os aplicativos também têm permissões que são independentes do espaço de trabalho, então podemos compartilhar este aplicativo com um público muito maior sem comprometer as configurações do espaço de trabalho ou ter que criar um novo.
- Fonte única de verdade: podemos colocar painéis, planilhas, conjuntos de dados e relatórios em um só lugar em um aplicativo, para que as informações sejam facilmente acessíveis.

![Aplicativos](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/power-bi-app-marketplace-08.png?_gl=1*15wbm2f*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4MzkzMTMuMzQuMC4w)

### **Selecionando um tipo de gráfico**
#### **Indicadores-chave de desempenho (KPIs)**
Então, como sabemos quais dados usar para nossos relatórios? O primeiro lugar onde devemos começar em nossa jornada de visualização é descobrir quais são as métricas mais importantes que queremos rastrear. Podemos usar essas métricas para criar indicadores-chave de desempenho (KPIs) — medições de negócios quantificáveis ​​— no painel que dão aos usuários finais uma imagem rápida e de alto nível de onde essas métricas estão.

Podemos definir um KPI no Power BI com um único número, às vezes codificado por cores para que o usuário saiba se o número é bom ou ruim. Juntos, esses KPIs se tornam os benchmarks para a história que estamos tentando contar. Existem alguns tipos diferentes de visualização de KPI no Power BI:

- Cartão : Um cartão nos permite mostrar um único número. Esta é uma única métrica que queremos rastrear.
- Cartão de várias linhas : se quisermos mostrar mais detalhes sobre a métrica que escolhemos, podemos usar um cartão de várias linhas para mostrar mais informações sobre a métrica ou relacionadas a ela.
- KPI : visualizações de KPI são um pouco mais complexas do que cartões. Essas visualizações também incluem uma tendência e uma meta, além do - indicador. Isso seria útil quando há uma meta clara para uma métrica e uma tendência ao longo do tempo é útil.
- Gauge Charts : Uma visualização de gauge é útil ao rastrear o progresso em direção a uma meta. É semelhante à visualização de KPI, pois temos uma meta, mas é mais específica para a métrica no sentido de que estamos olhando para um intervalo de valores em vez de uma tendência.

![KPIs](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/card-creation-09.gif?_gl=1*myyc15*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4MzkzMTMuMzQuMC4w)

#### **Gráficos de comparação**
Ao analisar dados, precisamos nos perguntar: "que pergunta estou tentando responder com os dados?" Um dos primeiros lugares que geralmente começamos depois de criar nossos KPIs é fazer algum tipo de comparação entre categorias dentro do conjunto de dados. Ao comparar diferentes categorias visualmente usando medidas, podemos começar a identificar perguntas adicionais dentro dos dados. Dois exemplos são:

- Gráficos de colunas : gráficos de colunas são usados ​​quando não há muitas categorias. Quando há muitas categorias, esse tipo de gráfico tende a se tornar ilegível.
- Gráficos de barras : quando o número de categorias se torna muito grande para o espaço ou os nomes das categorias são muito longos, é melhor usar um gráfico de barras.

![gcomparacao](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/comparison-chart-creation-10.gif?_gl=1*dd84py*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4MzkzMTMuMzQuMC4w)

#### **Gráficos de composição**
Os gráficos de composição são usados ​​para ver quanto das diferentes categorias inteiras compõem. Semelhantes aos gráficos de Barras e Colunas, eles exigem uma categoria com vários valores e alguma agregação. Alguns exemplos de gráficos de composição são:

- Gráficos de área : os gráficos de área são mais bem utilizados ao comparar tendências de volume em uma série temporal.
Barras empilhadas (recomendado) : o gráfico de barras empilhadas é usado para entender a contribuição de diferentes categorias para uma métrica.
- Gráficos de pizza/rosquinha (não recomendados) : embora sejam tipos de visualização padrão no Power BI, é recomendável ficar longe desses tipos de gráficos. Quando mais do que algumas categorias são adicionadas a esses gráficos, eles se tornam difíceis de ler.

![gcomposicao](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/composition-chart-creation-11.gif?_gl=1*sc9dkg*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4MzkzMTMuMzQuMC4w)

#### **Gráficos de distribuição**
Os gráficos de distribuição são usados ​​para visualizar muitos pontos de dados ao mesmo tempo. Eles podem consistir em uma ou duas medidas e uma dimensão. Os gráficos de distribuição são usados ​​quando há muitos pontos de dados que podem ser resumidos bem em grupos. Alguns exemplos de gráficos de distribuição são:

- Mapa de calor/Gráfico de área (usado para análise de tabelas) : Mapas de calor são usados ​​para identificar pontos críticos nos dados e nos permitem identificar rapidamente valores discrepantes nos dados.
- Gráfico de dispersão (usado para análise gráfica) : gráficos de dispersão são úteis quando temos várias métricas e gostaríamos de ver a relação entre elas, juntamente com as categorias.
- Gráfico espacial/geográfico (usado para análise visual geográfica) : mapas são usados ​​para representar graficamente métricas com base na localização.
- Mapa de árvore : mapas de árvore são usados ​​quando há um grande número de categorias e um gráfico de barras não consegue transmitir a mensagem.

![gdistribuicao](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/distribution-chart-creation-12.gif?_gl=1*sc9dkg*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4MzkzMTMuMzQuMC4w)

#### **Gráficos de tendências**
Os gráficos de tendência são usados ​​quando queremos rastrear algo ao longo do tempo. Esses gráficos fornecem contexto adicional aos nossos dados porque, às vezes, um único ponto pode ser enganoso. Às vezes, há tendências que nos permitem ter mais insights sobre o conjunto de dados, como sazonalidade, outliers e tendências. Alguns exemplos de gráficos de tendência são:

- Linha (usado em análise de séries temporais) : Gráficos de linha são úteis para identificar tendências nos dados ao longo do tempo. Eles podem ser usados ​​para representar visualmente os dados ao longo do tempo e nos ajudar a entender se há tendências nos dados.
- Coluna (usado em análise de séries temporais) : gráficos de colunas são úteis ao rastrear dados ao longo do tempo também. Semelhantes aos gráficos de linhas, eles podem ser usados ​​para identificar tendências e outliers.
- Gráfico de Gantt (usado no planejamento de projetos) : Um gráfico de Gantt é usado para rastrear um projeto ao longo do tempo. Isso pode fornecer insights valiosos sobre se o projeto está no caminho certo ou não.

#### **Fluxogramas**
Os fluxogramas são semelhantes aos gráficos de tendências, mas (como o nome sugere) mostram o volume de dados que fluem por um processo ou categorias.

![fluxograma1](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/power-bi-funnel-chart-14.png?_gl=1*1fr55i2*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4MzkzMTMuMzQuMC4w)

Alguns exemplos de fluxogramas são:

- Gráficos de Sankey: Em um gráfico de Sankey, as setas são proporcionais à taxa de fluxo.
- Gráfico de cascata: Um gráfico de cascata mostra um total em execução com base na soma/contagem cumulativa de valores em diferentes categorias. Isso é usado ao tentar descobrir como chegamos do início ao fim e todos os fatores entre eles.
- Gráficos de funil/pipeline: Um gráfico de funil é usado para mostrar a diferença entre diferentes estágios em um processo. Isso é mais comumente usado ao rastrear equipes de vendas.
- Árvore de decomposição: A árvore de decomposição é uma das visualizações de próxima geração que o Power BI tem a oferecer. Isso nos permite visualizar dados em diferentes dimensões e dividir os dados por categoria. Isso pode ser usado na análise de causa raiz para descobrir todos os fatores que podem estar influenciando os dados.

![fluxograma2](https://static-assets.codecademy.com/Courses/bi-dashboards-power-bi/basic-visualizations/decomposition-tree-16.png?_gl=1*1o1fafp*_gcl_au*MTU0OTEyNzE0MC4xNzE5MjM2NDA2*_ga*MDc0Mjg3MjY3Ni4xNzE5MjM2NDA5*_ga_3LRZM6TM9L*MTcyMTgzOTI4Ny4yNy4xLjE3MjE4MzkzMTMuMzQuMC4w)