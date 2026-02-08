# TP MST - Ejercicios 2 y 3

Soluciones en Python para los ejercicios de Árboles de Expansión Mínima (MST) y Dijkstra.

## 📁 Archivos

- **`ejercicio2_mst.py`** - Implementación de algoritmos de Prim y Kruskal para MST
- **`ejercicio3_dijkstra.py`** - Implementación del algoritmo de Dijkstra para caminos más cortos

## 🚀 Cómo ejecutar

### Ejercicio 2 (MST - Prim y Kruskal)

```bash
python ejercicio2_mst.py
```

Este programa:
- Crea un grafo con 8 distritos
- Encuentra el Árbol de Expansión Mínima usando **Prim** y **Kruskal**
- Muestra el proceso paso a paso
- Compara los resultados de ambos algoritmos

### Ejercicio 3 (Dijkstra)

```bash
python ejercicio3_dijkstra.py
```

Este programa:
- Simula una red de mensajería con almacén central y puntos de entrega
- Encuentra el camino más corto desde el almacén a cada destino usando **Dijkstra**
- Muestra el proceso de exploración paso a paso
- Incluye un ejemplo bonus con rutas dirigidas (calles de una sola vía)

## 📚 Conceptos Clave

### Ejercicio 2: MST (Minimum Spanning Tree)

**Problema**: Conectar 8 distritos con fibra óptica minimizando el costo total.

**Algoritmos implementados**:

1. **Prim**: 
   - Empieza desde un nodo y va creciendo el árbol
   - Siempre elige la arista más barata que conecte un nodo nuevo
   - Es como ir construyendo la red paso a paso, eligiendo siempre la opción más económica

2. **Kruskal**:
   - Ordena todas las aristas por costo
   - Va agregando aristas de menor a mayor costo
   - Rechaza aristas que formarían ciclos
   - Es como ir eligiendo las mejores ofertas, pero evitando redundancias

**Estructuras de datos usadas**:
- Lista de adyacencia para representar el grafo
- Min-heap (cola de prioridad) para Prim
- Union-Find para detectar ciclos en Kruskal

### Ejercicio 3: Dijkstra

**Problema**: Encontrar el camino más rápido desde un almacén central a todos los puntos de entrega.

**Algoritmo de Dijkstra**:
- Encuentra el camino más corto desde un nodo origen a TODOS los demás
- Usa un enfoque greedy: siempre explora el nodo más cercano primero
- Es como Google Maps: te dice la ruta más rápida a cada destino

**Características**:
- Funciona con grafos dirigidos y no dirigidos
- Maneja rutas de una sola vía (calles de sentido único)
- Reconstruye el camino completo, no solo la distancia

## 🎯 Características de las implementaciones

✅ **Código bien documentado** con explicaciones en tono coloquial  
✅ **Visualización paso a paso** del proceso de cada algoritmo  
✅ **Nombres descriptivos** para variables y funciones  
✅ **Ejemplos realistas** con contexto del problema  
✅ **Análisis de resultados** con estadísticas adicionales  

## 💡 Tips para modificar los ejemplos

### Cambiar el grafo del Ejercicio 2:

```python
# En la función main() de ejercicio2_mst.py
conexiones_disponibles = [
    (0, 1, 4),   # Distrito 0 a 1: costo 4
    (0, 2, 3),   # Agrega más conexiones aquí
    # ...
]
```

### Cambiar el grafo del Ejercicio 3:

```python
# En la función main() de ejercicio3_dijkstra.py
rutas = [
    (0, 1, 10),  # Almacén → Zona Norte: 10 min
    (0, 2, 15),  # Agrega más rutas aquí
    # ...
]
```

## 🔍 Complejidad de los algoritmos

| Algoritmo | Complejidad (con heap) | Mejor para |
|-----------|------------------------|------------|
| **Prim** | O((V + E) log V) | Grafos densos |
| **Kruskal** | O(E log E) | Grafos dispersos |
| **Dijkstra** | O((V + E) log V) | Caminos más cortos |

Donde:
- V = número de vértices (nodos)
- E = número de aristas (conexiones)

## 📝 Notas del alumno

- **MST**: Ambos algoritmos (Prim y Kruskal) encuentran un MST con el mismo costo mínimo, pero las aristas elegidas pueden variar si hay empates.
  
- **Dijkstra**: Solo funciona con pesos positivos. Si tenés pesos negativos, necesitás Bellman-Ford.

- **Union-Find**: Es una estructura de datos clave para Kruskal. Permite detectar ciclos de forma eficiente.

## 🐛 Troubleshooting

**Error: `ModuleNotFoundError: No module named 'heapq'`**
- No debería pasar, `heapq` es parte de la biblioteca estándar de Python

**El programa no muestra nada**
- Asegurate de estar ejecutando con `python ejercicio2_mst.py` o `python ejercicio3_dijkstra.py`

**Los resultados no coinciden con lo esperado**
- Verificá que los datos del grafo estén bien ingresados
- Recordá que puede haber múltiples MST válidos con el mismo costo

## 📖 Referencias

- Cormen, T. H., et al. (2009). *Introduction to Algorithms* (3rd ed.)
- Material de clase de Programación III
- [Visualización de algoritmos](https://visualgo.net/) - Excelente para entender cómo funcionan

---

**Autor**: Estudiante de Programación III  
**Fecha**: Febrero 2026  
**Curso**: Desarrollo 2026 Verano
