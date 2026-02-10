# Algoritmo de Floyd-Warshall

El algoritmo de Floyd-Warshall es un algoritmo de programación dinámica utilizado para encontrar los caminos más cortos entre **todos los pares de vértices** en un grafo dirigido y ponderado. Es capaz de manejar pesos de arista positivos y negativos, pero no puede manejar ciclos negativos a los que se pueda llegar desde un par de vértices (si existe un ciclo negativo, el algoritmo podría dar un resultado incorrecto, o los valores en la diagonal principal de la matriz resultante serían negativos, indicando la presencia de dicho ciclo).

## Propósito

El objetivo principal del algoritmo de Floyd-Warshall es calcular una matriz de distancias `dist` donde `dist[i][j]` representa la longitud del camino más corto desde el vértice `i` hasta el vértice `j`.

## ¿Cómo funciona?

El algoritmo opera iterativamente, considerando todos los vértices del grafo como posibles "vértices intermedios" en los caminos más cortos.

1.  **Inicialización:**
    Se inicializa una matriz de distancias `dist` con los pesos de las aristas directas entre cada par de vértices.
    *   `dist[i][j]` = `weight(i, j)` si existe una arista directa de `i` a `j`.
    *   `dist[i][j]` = `INF` (infinito) si no existe una arista directa.
    *   `dist[i][i]` = `0` (la distancia de un vértice a sí mismo es cero).

2.  **Iteración:**
    El algoritmo realiza `N` iteraciones (donde `N` es el número de vértices en el grafo). En cada iteración `k` (de `0` a `N-1`), considera que el vértice `k` puede ser un vértice intermedio en un camino más corto entre cualquier par de vértices `(i, j)`.

    Para cada par `(i, j)`, el algoritmo actualiza `dist[i][j]` con la siguiente fórmula:
    `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

    Esto significa que el camino más corto de `i` a `j` es el mínimo entre:
    *   El camino más corto actual que no usa `k` como intermedio.
    *   El camino más corto que va de `i` a `k`, y luego de `k` a `j`.

## Complejidad

La complejidad temporal del algoritmo de Floyd-Warshall es **O(V^3)**, donde `V` es el número de vértices en el grafo. Esto se debe a los tres bucles anidados que recorren `k`, `i` y `j` de `0` a `V-1`.

La complejidad espacial es **O(V^2)** para almacenar la matriz de distancias.

## Interpretación de la Matriz de Salida

*   **Valores finitos y positivos/negativos:** `dist[i][j]` contendrá el peso del camino más corto.
*   **`INF` (Infinito):** Si `dist[i][j]` sigue siendo `INF` después de la ejecución del algoritmo, significa que no hay un camino posible desde el vértice `i` hasta el vértice `j`.
*   **Valores negativos en la diagonal (`dist[i][i] < 0`):** Si, después de todas las iteraciones, `dist[i][i]` es negativo para cualquier vértice `i`, esto indica la presencia de un **ciclo negativo** accesible desde (y a) el vértice `i`. En tales casos, los caminos más cortos que involucran este ciclo negativo son indefinidos (pueden ser arbitrariamente pequeños).

## Consideraciones sobre `math.inf` y Ciclos Negativos

*   **`math.inf`:** Se utiliza para representar la ausencia de una conexión directa o un camino infinitamente largo. En Python, `float('inf')` o `math.inf` es adecuado.
*   **Ciclos Negativos:** Aunque Floyd-Warshall puede detectar ciclos negativos (mediante la verificación de la diagonal principal), no puede encontrar los "caminos más cortos" en presencia de tales ciclos, ya que un camino puede volverse arbitrariamente corto al recorrer repetidamente el ciclo negativo. Si se detecta un ciclo negativo, se debe interpretar que el concepto de "camino más corto" no es aplicable para los vértices afectados.
