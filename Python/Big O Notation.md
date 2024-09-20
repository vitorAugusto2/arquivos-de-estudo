# Big O Notation
Big O Notation é uma forma de medir a **eficiência** de um algoritmo, considerando dois aspectos principais: **complexidade de tempo** e **complexidade de espaço**. Ela descreve como o desempenho de um algoritmo muda conforme o tamanho da entrada (n) aumenta.

## Complexidade de Tempo
Refere-se ao número de operações ou tempo que o algoritmo leva para ser executado conforme o tamanho da entrada. O **melhor algoritmo** é aquele cujo tempo de execução **cresce mais lentamente** à medida que a entrada aumenta, ou seja, ele é eficiente mesmo para grandes quantidades de dados.

- Exemplo: Um algoritmo com complexidade **O(1)** executa no mesmo tempo independentemente do tamanho da entrada, enquanto **O(n)** cresce linearmente com o tamanho da entrada.

## Complexidade de Espaço
Mede a quantidade de **memória extra** necessária para a execução de um algoritmo em relação ao tamanho da entrada. Algoritmos que utilizam menos memória são preferíveis.

- Exemplo: Um algoritmo que cria uma cópia de um array. Neste caso, a quantidade de memória necessária aumenta proporcionalmente ao tamanho da entrada, ou seja, **O(n)**.

## Questões Importantes
1. O código pode **ficar mais lento** à medida que a quantidade de dados aumenta.
2. A análise de Big O é ***independente do hardware**: ela considera apenas o número de operações, não o tempo exato em segundos.
3. Big O **ignora constantes e operações menores**. Por exemplo, **O(n + 1)** é simplificado para **O(n)**, porque o termo dominante é mais importante à medida que n cresce.

## Gráfico Big O
![image](https://github.com/user-attachments/assets/d22eeea9-9c92-425c-9eb5-406c132d9dce)

As seguintes anotações representam os diferentes tipos de crescimento de complexidade:

### O(1) – Tempo Constante
O tempo de execução não depende do tamanho da entrada.
- Exemplo: Acesso direto a um elemento de um array.

### O(log n) – Tempo Logarítmico
O tempo de execução **diminui significativamente** conforme o tamanho da entrada aumenta.
- Exemplo: Busca binária.

### O(n) – Tempo Linear
O tempo de execução **cresce linearmente** com o tamanho da entrada.
- Exemplo: Percorrer todos os elementos de uma lista.

### O(n log n) – Tempo Quase Linear
O tempo de execução é um pouco pior que O(n), mas ainda é muito mais eficiente que O(n²) para grandes entradas.
- Exemplo: Algoritmos de ordenação eficientes como quicksort, mergesort e heapsort.

### O(n²) – Tempo Quadrático
O tempo de execução aumenta rapidamente conforme o tamanho da entrada aumenta.
- Exemplo: Algoritmos de ordenação ineficientes como bubblesort, insertion sort e selection sort.

### O(n!) – Tempo Fatorial
O tempo de execução cresce de maneira explosiva à medida que o tamanho da entrada aumenta. Usado apenas para pequenos problemas.
- Exemplo: Problema do caixeiro viajante (_brute force_).

## Conclusão
Big O Notation nos ajuda a **comparar e escolher algoritmos** com base em como eles escalam. Um bom algoritmo é aquele que pode lidar eficientemente com grandes quantidades de dados tanto em termos de tempo quanto de memória.
