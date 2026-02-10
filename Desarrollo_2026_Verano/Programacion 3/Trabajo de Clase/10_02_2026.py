import math

def floyd_warshall(graph):
    """
    Implementa el algoritmo de Floyd-Warshall para encontrar los caminos más cortos entre todos los pares de nodos.

    Args:
        graph (list of list of int): Una matriz de adyacencia que representa el grafo.
                                      graph[i][j] es el peso del borde de i a j.
                                      Un valor de math.inf indica que no hay borde directo.
                                      Un valor de 0 en graph[i][i] es esperado.

    Returns:
        list of list of int: Una matriz que contiene las distancias de los caminos más cortos entre todos los pares de nodos.
    """
    num_vertices = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # Algoritmo principal de Floyd-Warshall
    for k in range(num_vertices):
        # Escoge todos los vértices como intermedios uno por uno
        for i in range(num_vertices):
            # Escoge todos los vértices como fuente uno por uno
            for j in range(num_vertices):
                # Si el vértice k está en el camino más corto de i a j,
                # entonces actualiza el valor de dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def print_solution(dist):
    """
    Imprime la matriz de distancias resultantes.
    """
    print("La siguiente matriz muestra las distancias más cortas entre cada par de vértices:")
    for i in range(len(dist)):
        for j in range(len(dist[0])):
            if dist[i][j] == math.inf:
                print("%7s" % "INF", end=" ")
            else:
                print("%7d" % dist[i][j], end=" ")
        print()

def run_tests():
    """
    Ejecuta casos de prueba para el algoritmo de Floyd-Warshall.
    """
    print("--- Caso de Prueba 1: Grafo simple ---")
    graph1 = [
        [0, 3, math.inf, 7],
        [8, 0, 2, math.inf],
        [5, math.inf, 0, 1],
        [2, math.inf, math.inf, 0]
    ]
    solution1 = [
        [0, 3, 5, 6],
        [5, 0, 2, 3],
        [3, 6, 0, 1],
        [2, 5, 7, 0]
    ]
    result1 = floyd_warshall(graph1)
    print("Grafo de entrada 1:")
    print_solution(graph1)
    print("\nSolución esperada 1:")
    print_solution(solution1)
    print("\nResultado obtenido 1:")
    print_solution(result1)
    assert result1 == solution1, "El caso de prueba 1 falló."
    print("Caso de prueba 1 PASÓ.\n")

    print("--- Caso de Prueba 2: Grafo con desconexiones y pesos grandes ---")
    graph2 = [
        [0, 5, math.inf, 10],
        [math.inf, 0, 3, math.inf],
        [math.inf, math.inf, 0, 1],
        [math.inf, math.inf, math.inf, 0]
    ]
    solution2 = [
        [0, 5, 8, 9],
        [math.inf, 0, 3, 4],
        [math.inf, math.inf, 0, 1],
        [math.inf, math.inf, math.inf, 0]
    ]
    result2 = floyd_warshall(graph2)
    print("Grafo de entrada 2:")
    print_solution(graph2)
    print("\nSolución esperada 2:")
    print_solution(solution2)
    print("\nResultado obtenido 2:")
    print_solution(result2)
    assert result2 == solution2, "El caso de prueba 2 falló."
    print("Caso de prueba 2 PASÓ.\n")

    print("--- Caso de Prueba 3: Grafo con un solo vértice ---")
    graph3 = [
        [0]
    ]
    solution3 = [
        [0]
    ]
    result3 = floyd_warshall(graph3)
    print("Grafo de entrada 3:")
    print_solution(graph3)
    print("\nSolución esperada 3:")
    print_solution(solution3)
    print("\nResultado obtenido 3:")
    print_solution(result3)
    assert result3 == solution3, "El caso de prueba 3 falló."
    print("Caso de prueba 3 PASÓ.\n")

    print("--- Caso de Prueba 4: Grafo con ciclos negativos (pero no detectados por Floyd-Warshall directamente) ---")
    # Floyd-Warshall detectará los caminos más cortos, pero no explícitamente si hay un ciclo negativo
    # que haga que un camino sea infinitamente más corto.
    # Para este ejemplo, asegúrate de que no haya ciclos negativos accesibles desde el origen que lleven a -infinito.
    # El algoritmo de Floyd-Warshall estándar aún calculará los caminos más cortos,
    # pero si hay un ciclo negativo, los valores en la diagonal principal podrían volverse negativos después de la ejecución.
    graph4 = [
        [0, 1, math.inf],
        [math.inf, 0, -1],
        [-2, math.inf, 0]
    ]
    solution4 = [
        [-2, -1, -2],
        [-3, -2, -3],
        [-4, -3, -4]
    ]
    result4 = floyd_warshall(graph4)
    print("Grafo de entrada 4:")
    print_solution(graph4)
    print("\nSolución esperada 4:")
    print_solution(solution4)
    print("\nResultado obtenido 4:")
    print_solution(result4)
    assert result4 == solution4, "El caso de prueba 4 falló."
    # Para detectar ciclos negativos, se debería comprobar si dist[i][i] < 0 después de ejecutar el algoritmo.
    # Aquí solo estamos verificando que los caminos más cortos se calculen correctamente.
    print("Caso de prueba 4 PASÓ.\n")

    print("Todos los casos de prueba han pasado exitosamente!")


if __name__ == "__main__":
    run_tests()
