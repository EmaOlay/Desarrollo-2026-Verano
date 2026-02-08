"""
EJERCICIO 2: Árbol de Expansión Mínima (MST)
Problema: Conectar 8 distritos con fibra óptica minimizando costos

Este código implementa dos algoritmos clásicos para encontrar el MST:
- Algoritmo de Prim: Va creciendo el árbol desde un nodo inicial
- Algoritmo de Kruskal: Ordena todas las aristas y las va agregando si no forman ciclos

"""

import sys
import heapq
from typing import List, Tuple, Dict



class UnionFind:
    """
    Estructura de datos para detectar ciclos (usada en Kruskal)
    
    Básicamente es como tener grupos de amigos: si dos personas ya están
    en el mismo grupo, no necesitas presentarlas de nuevo.
    """
    
    def __init__(self, n: int):
        # Cada nodo empieza siendo su propio padre (está solo)
        self.parent = list(range(n))
        # El rango ayuda a mantener el árbol balanceado
        self.rank = [0] * n
    
    def find(self, x: int) -> int:
        """Encuentra el representante del grupo de x"""
        if self.parent[x] != x:
            # Path compression: optimización para hacer búsquedas más rápidas
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        """
        Une los grupos de x e y
        Retorna True si se unieron, False si ya estaban en el mismo grupo
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Ya están conectados, sería un ciclo
        
        # Union by rank: el árbol más pequeño se pega al más grande
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True


class GrafoDistritos:
    """
    Representa la red de distritos y sus conexiones
    """
    
    def __init__(self, num_distritos: int):
        self.num_distritos = num_distritos
        # Usamos lista de adyacencia: más eficiente para grafos dispersos
        self.adyacencia: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(num_distritos)}
        # También guardamos todas las aristas para Kruskal
        self.aristas: List[Tuple[int, int, int]] = []
    
    def agregar_conexion(self, distrito1: int, distrito2: int, costo: int):
        """Agrega una conexión bidireccional entre dos distritos"""
        self.adyacencia[distrito1].append((distrito2, costo))
        self.adyacencia[distrito2].append((distrito1, costo))
        # Guardamos la arista una sola vez para Kruskal
        self.aristas.append((costo, distrito1, distrito2))
    
    def prim(self, inicio: int = 0) -> Tuple[List[Tuple[int, int, int]], int]:
        """
        Algoritmo de Prim para encontrar el MST
        
        La idea: empezamos desde un distrito y vamos agregando la conexión
        más barata que nos lleve a un distrito nuevo (no visitado).
        Es como ir construyendo la red paso a paso, siempre eligiendo
        la opción más económica disponible.
        
        Returns:
            - Lista de conexiones (distrito1, distrito2, costo)
            - Costo total
        """
        print("\n" + "="*60)
        print("ALGORITMO DE PRIM - Construcción paso a paso")
        print("="*60)
        
        visitados = set([inicio])
        mst_conexiones = []
        costo_total = 0
        
        # Min-heap con las aristas disponibles: (costo, desde, hacia)
        heap = [(costo, inicio, vecino) for vecino, costo in self.adyacencia[inicio]]
        heapq.heapify(heap)
        
        paso = 1
        
        while heap and len(visitados) < self.num_distritos:
            costo, desde, hacia = heapq.heappop(heap)
            
            # Si ya visitamos este distrito, skip
            if hacia in visitados:
                continue
            
            # ¡Agregamos esta conexión al MST!
            visitados.add(hacia)
            mst_conexiones.append((desde, hacia, costo))
            costo_total += costo
            
            print(f"\nPaso {paso}:")
            print(f"  Conectamos Distrito {desde} -> Distrito {hacia}")
            print(f"  Costo de esta conexión: ${costo}")
            print(f"  Costo acumulado: ${costo_total}")
            print(f"  Distritos conectados: {sorted(visitados)}")
            
            # Agregamos las nuevas aristas disponibles desde el distrito recién agregado
            for vecino, costo_vecino in self.adyacencia[hacia]:
                if vecino not in visitados:
                    heapq.heappush(heap, (costo_vecino, hacia, vecino))
            
            paso += 1
        
        return mst_conexiones, costo_total
    
    def kruskal(self) -> Tuple[List[Tuple[int, int, int]], int]:
        """
        Algoritmo de Kruskal para encontrar el MST
        
        La idea: ordenamos todas las conexiones de más barata a más cara,
        y vamos agregando cada una SI NO forma un ciclo.
        Es como ir eligiendo las mejores ofertas, pero asegurándonos
        de no conectar cosas que ya están conectadas.
        
        Returns:
            - Lista de conexiones (distrito1, distrito2, costo)
            - Costo total
        """
        print("\n" + "="*60)
        print("ALGORITMO DE KRUSKAL - Construcción paso a paso")
        print("="*60)
        
        # Ordenamos las aristas por costo (de menor a mayor)
        aristas_ordenadas = sorted(self.aristas)
        
        uf = UnionFind(self.num_distritos)
        mst_conexiones = []
        costo_total = 0
        paso = 1
        
        print(f"\nTenemos {len(aristas_ordenadas)} conexiones posibles")
        print("Vamos a evaluarlas de la más barata a la más cara...\n")
        
        for costo, distrito1, distrito2 in aristas_ordenadas:
            # Intentamos unir estos dos distritos
            if uf.union(distrito1, distrito2):
                # ¡Se pudo! No formaba ciclo
                mst_conexiones.append((distrito1, distrito2, costo))
                costo_total += costo
                
                print(f"Paso {paso}:")
                print(f"  Agregamos: Distrito {distrito1} <-> Distrito {distrito2}")
                print(f"  Costo: ${costo}")
                print(f"  Costo acumulado: ${costo_total}")
                print(f"  Esta conexión NO forma ciclo\n")
                
                paso += 1
            else:
                # Ya estaban conectados, sería un ciclo
                print(f"  Rechazamos: Distrito {distrito1} <-> Distrito {distrito2} (costo ${costo})")
                print(f"    Razón: Ya están conectados por otro camino (formaría ciclo)\n")
            
            # Si ya tenemos n-1 aristas, terminamos
            if len(mst_conexiones) == self.num_distritos - 1:
                break
        
        return mst_conexiones, costo_total


def mostrar_resultado_final(conexiones: List[Tuple[int, int, int]], costo_total: int, algoritmo: str):
    """Muestra el resultado final de forma bonita"""
    print("\n" + "="*60)
    print(f"RESULTADO FINAL - {algoritmo}")
    print("="*60)
    print("\nRed de Fibra Óptica Óptima:\n")
    
    for i, (d1, d2, costo) in enumerate(conexiones, 1):
        print(f"  {i}. Distrito {d1} <-> Distrito {d2} | Costo: ${costo}")
    
    print(f"\nCOSTO TOTAL DE LA INFRAESTRUCTURA: ${costo_total}")
    print("="*60 + "\n")


def main():
    """
    Ejemplo con 8 distritos como pide el ejercicio
    """
    print("\nPROBLEMA: Red de Fibra Óptica para 8 Distritos")
    print("="*60)
    print("Necesitamos conectar todos los distritos minimizando el costo")
    print("de instalación de fibra óptica.\n")
    
    # Creamos el grafo con 8 distritos
    grafo = GrafoDistritos(8)
    
    # Agregamos las conexiones (distrito1, distrito2, costo)
    # Este es un ejemplo, puedes cambiarlo por los datos reales
    conexiones_disponibles = [
        (0, 1, 4),   # Distrito 0 a 1: costo 4
        (0, 2, 3),   # Distrito 0 a 2: costo 3
        (1, 2, 1),   # Distrito 1 a 2: costo 1
        (1, 3, 2),   # Distrito 1 a 3: costo 2
        (2, 3, 4),   # Distrito 2 a 3: costo 4
        (2, 4, 5),   # Distrito 2 a 4: costo 5
        (3, 4, 1),   # Distrito 3 a 4: costo 1
        (3, 5, 6),   # Distrito 3 a 5: costo 6
        (4, 5, 2),   # Distrito 4 a 5: costo 2
        (4, 6, 3),   # Distrito 4 a 6: costo 3
        (5, 6, 4),   # Distrito 5 a 6: costo 4
        (5, 7, 5),   # Distrito 5 a 7: costo 5
        (6, 7, 2),   # Distrito 6 a 7: costo 2
    ]
    
    print("Conexiones disponibles (senderos preexistentes):\n")
    for d1, d2, costo in conexiones_disponibles:
        grafo.agregar_conexion(d1, d2, costo)
        print(f"  Distrito {d1} <-> Distrito {d2}: ${costo}")
    
    # Ejecutamos Prim
    print("\n\n" + "="*60)
    print("MÉTODO 1: ALGORITMO DE PRIM")
    print("="*60)
    conexiones_prim, costo_prim = grafo.prim(inicio=0)
    mostrar_resultado_final(conexiones_prim, costo_prim, "PRIM")
    
    # Ejecutamos Kruskal
    print("\n" + "="*60)
    print("MÉTODO 2: ALGORITMO DE KRUSKAL")
    print("="*60)
    conexiones_kruskal, costo_kruskal = grafo.kruskal()
    mostrar_resultado_final(conexiones_kruskal, costo_kruskal, "KRUSKAL")
    
    # Verificación
    print("\n" + "="*60)
    print("CONCLUSIÓN")
    print("="*60)
    print(f"Ambos algoritmos encontraron un MST con costo: ${costo_prim}")
    print("(Puede haber diferentes MST con el mismo costo si hay empates)")
    print("\nLa red óptima conecta todos los distritos con el mínimo costo posible.")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
