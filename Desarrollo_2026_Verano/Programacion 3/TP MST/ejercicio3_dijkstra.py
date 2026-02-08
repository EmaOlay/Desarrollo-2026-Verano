"""
EJERCICIO 3: Algoritmo de Dijkstra
Problema: Encontrar el camino más rápido desde un almacén central
          a todos los puntos de entrega

Este código implementa el algoritmo de Dijkstra para encontrar
el camino más corto desde un nodo origen a todos los demás.

Básicamente, es como Google Maps pero para tu empresa de mensajería:
te dice cuál es la ruta más rápida a cada destino.

"""

import sys
import heapq
from typing import List, Tuple, Dict, Optional



class GrafoMensajeria:
    """
    Representa la red de rutas de la empresa de mensajería
    """
    
    def __init__(self, num_puntos: int):
        self.num_puntos = num_puntos
        # Lista de adyacencia: {nodo: [(vecino, tiempo/costo), ...]}
        self.adyacencia: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(num_puntos)}
        self.nombres_puntos: Dict[int, str] = {}
    
    def agregar_ruta(self, origen: int, destino: int, tiempo: int):
        """
        Agrega una ruta DIRIGIDA desde origen a destino
        (las rutas pueden ser de una sola vía)
        """
        self.adyacencia[origen].append((destino, tiempo))
    
    def agregar_ruta_bidireccional(self, punto1: int, punto2: int, tiempo: int):
        """
        Agrega una ruta que se puede recorrer en ambas direcciones
        """
        self.adyacencia[punto1].append((punto2, tiempo))
        self.adyacencia[punto2].append((punto1, tiempo))
    
    def asignar_nombre(self, punto: int, nombre: str):
        """Asigna un nombre descriptivo a un punto"""
        self.nombres_puntos[punto] = nombre
    
    def obtener_nombre(self, punto: int) -> str:
        """Obtiene el nombre de un punto o su número si no tiene nombre"""
        return self.nombres_puntos.get(punto, f"Punto {punto}")
    
    def dijkstra(self, almacen: int) -> Tuple[List[int], List[Optional[int]]]:
        """
        Algoritmo de Dijkstra para encontrar el camino más corto
        desde el almacén a todos los demás puntos.
        
        La idea: empezamos desde el almacén con distancia 0.
        Vamos explorando los vecinos más cercanos primero (greedy approach).
        Cada vez que encontramos un camino más corto a un punto,
        actualizamos su distancia.
        
        Es como ir expandiendo una mancha de aceite: primero llega
        a los lugares cercanos, luego a los más lejanos.
        
        Returns:
            - distancias: lista con la distancia mínima a cada punto
            - predecesores: lista que nos permite reconstruir el camino
        """
        print("\n" + "="*70)
        print(f"ALGORITMO DE DIJKSTRA - Desde {self.obtener_nombre(almacen)}")
        print("="*70)
        
        # Inicialización
        distancias = [float('inf')] * self.num_puntos
        distancias[almacen] = 0
        predecesores = [None] * self.num_puntos
        visitados = set()
        
        # Min-heap: (distancia, nodo)
        heap = [(0, almacen)]
        
        print(f"\nIniciando desde {self.obtener_nombre(almacen)}")
        print(f"Tenemos que encontrar el camino más corto a {self.num_puntos - 1} destinos\n")
        
        paso = 1
        
        while heap:
            dist_actual, nodo_actual = heapq.heappop(heap)
            
            # Si ya visitamos este nodo, skip
            if nodo_actual in visitados:
                continue
            
            visitados.add(nodo_actual)
            
            print(f"Paso {paso}: Explorando {self.obtener_nombre(nodo_actual)}")
            print(f"  Distancia desde almacén: {dist_actual}")
            
            # Exploramos todos los vecinos
            vecinos_mejorados = []
            for vecino, tiempo in self.adyacencia[nodo_actual]:
                if vecino in visitados:
                    continue
                
                nueva_distancia = dist_actual + tiempo
                
                # ¿Encontramos un camino más corto?
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual
                    heapq.heappush(heap, (nueva_distancia, vecino))
                    vecinos_mejorados.append((vecino, tiempo, nueva_distancia))
            
            if vecinos_mejorados:
                print(f"  Actualizamos distancias:")
                for vecino, tiempo, nueva_dist in vecinos_mejorados:
                    print(f"    -> {self.obtener_nombre(vecino)}: "
                          f"{dist_actual} + {tiempo} = {nueva_dist}")
            else:
                print(f"  No hay vecinos nuevos por explorar")
            
            print()
            paso += 1
        
        return distancias, predecesores
    
    def reconstruir_camino(self, destino: int, predecesores: List[Optional[int]]) -> List[int]:
        """
        Reconstruye el camino desde el almacén hasta un destino
        usando la lista de predecesores
        """
        if predecesores[destino] is None:
            return [destino]
        
        camino = []
        actual = destino
        
        while actual is not None:
            camino.append(actual)
            actual = predecesores[actual]
        
        return list(reversed(camino))
    
    def mostrar_resultados(self, almacen: int, distancias: List[int], 
                          predecesores: List[Optional[int]]):
        """Muestra los resultados de forma clara y bonita"""
        print("="*70)
        print("RESULTADOS FINALES - RUTAS ÓPTIMAS DE ENTREGA")
        print("="*70)
        print(f"\nDesde: {self.obtener_nombre(almacen)}\n")
        
        # Ordenamos por distancia para mostrar primero los más cercanos
        destinos_ordenados = [(i, distancias[i]) for i in range(self.num_puntos) if i != almacen]
        destinos_ordenados.sort(key=lambda x: x[1])
        
        for destino, distancia in destinos_ordenados:
            if distancia == float('inf'):
                print(f"[X] {self.obtener_nombre(destino)}: INALCANZABLE")
                continue
            
            camino = self.reconstruir_camino(destino, predecesores)
            camino_str = " -> ".join([self.obtener_nombre(p) for p in camino])
            
            print(f"[OK] {self.obtener_nombre(destino)}:")
            print(f"   Tiempo mínimo: {distancia} minutos")
            print(f"   Ruta: {camino_str}")
            print()
        
        print("="*70)
        print("TIP: Estas son las rutas más rápidas para cada destino.")
        print("   Puedes optimizar tu logística usando esta información.")
        print("="*70 + "\n")


def main():
    """
    Ejemplo de uso: empresa de mensajería con almacén central
    y varios puntos de entrega
    """
    print("\nPROBLEMA: Optimización de Rutas de Mensajería")
    print("="*70)
    print("Una empresa de mensajería necesita encontrar las rutas más rápidas")
    print("desde su almacén central a todos los puntos de entrega.\n")
    
    # Creamos el grafo (ejemplo con 7 puntos)
    grafo = GrafoMensajeria(7)
    
    # Asignamos nombres descriptivos
    grafo.asignar_nombre(0, "Almacén Central")
    grafo.asignar_nombre(1, "Zona Norte")
    grafo.asignar_nombre(2, "Zona Sur")
    grafo.asignar_nombre(3, "Zona Este")
    grafo.asignar_nombre(4, "Zona Oeste")
    grafo.asignar_nombre(5, "Centro Comercial")
    grafo.asignar_nombre(6, "Zona Industrial")
    
    # Agregamos las rutas (bidireccionales en este caso)
    # Formato: (punto1, punto2, tiempo_en_minutos)
    rutas = [
        (0, 1, 10),  # Almacén → Zona Norte: 10 min
        (0, 2, 15),  # Almacén → Zona Sur: 15 min
        (0, 3, 20),  # Almacén → Zona Este: 20 min
        (1, 3, 5),   # Zona Norte → Zona Este: 5 min
        (1, 4, 12),  # Zona Norte → Zona Oeste: 12 min
        (2, 3, 8),   # Zona Sur → Zona Este: 8 min
        (2, 5, 7),   # Zona Sur → Centro Comercial: 7 min
        (3, 5, 6),   # Zona Este → Centro Comercial: 6 min
        (3, 6, 10),  # Zona Este → Zona Industrial: 10 min
        (4, 6, 9),   # Zona Oeste → Zona Industrial: 9 min
        (5, 6, 4),   # Centro Comercial → Zona Industrial: 4 min
    ]
    
    print("Red de rutas disponibles:\n")
    for p1, p2, tiempo in rutas:
        grafo.agregar_ruta_bidireccional(p1, p2, tiempo)
        print(f"  {grafo.obtener_nombre(p1)} <-> {grafo.obtener_nombre(p2)}: {tiempo} min")
    
    # Ejecutamos Dijkstra desde el almacén (nodo 0)
    almacen = 0
    distancias, predecesores = grafo.dijkstra(almacen)
    
    # Mostramos los resultados
    grafo.mostrar_resultados(almacen, distancias, predecesores)
    
    # Análisis adicional
    print("\n" + "="*70)
    print("ANÁLISIS ADICIONAL")
    print("="*70)
    
    # Destino más lejano
    destinos = [(i, distancias[i]) for i in range(grafo.num_puntos) if i != almacen]
    destino_mas_lejano = max(destinos, key=lambda x: x[1])
    destino_mas_cercano = min(destinos, key=lambda x: x[1])
    
    print(f"\nDestino más cercano: {grafo.obtener_nombre(destino_mas_cercano[0])} "
          f"({destino_mas_cercano[1]} min)")
    print(f"Destino más lejano: {grafo.obtener_nombre(destino_mas_lejano[0])} "
          f"({destino_mas_lejano[1]} min)")
    
    tiempo_total = sum(d for i, d in destinos if d != float('inf'))
    print(f"\nSi visitaras todos los destinos por separado (desde el almacén):")
    print(f"   Tiempo total acumulado: {tiempo_total} minutos")
    print(f"\nNota: En la práctica, optimizarías la ruta para visitar")
    print(f"   múltiples destinos en un solo viaje (problema del TSP).")
    print("="*70 + "\n")


def ejemplo_con_rutas_dirigidas():
    """
    Ejemplo adicional con rutas dirigidas (calles de una sola vía)
    """
    print("\n" + "="*70)
    print("EJEMPLO BONUS: Red con Calles de Una Sola Vía")
    print("="*70 + "\n")
    
    grafo = GrafoMensajeria(5)
    
    grafo.asignar_nombre(0, "Almacén")
    grafo.asignar_nombre(1, "Punto A")
    grafo.asignar_nombre(2, "Punto B")
    grafo.asignar_nombre(3, "Punto C")
    grafo.asignar_nombre(4, "Punto D")
    
    # Rutas dirigidas (solo se puede ir en una dirección)
    print("Red de rutas (algunas son de una sola vía):\n")
    
    rutas_dirigidas = [
        (0, 1, 5, True),   # Almacén → A (bidireccional)
        (0, 2, 10, True),  # Almacén → B (bidireccional)
        (1, 3, 3, False),  # A → C (solo ida)
        (2, 1, 2, False),  # B → A (solo ida)
        (2, 4, 7, True),   # B → D (bidireccional)
        (3, 4, 1, False),  # C → D (solo ida)
    ]
    
    for origen, destino, tiempo, bidireccional in rutas_dirigidas:
        if bidireccional:
            grafo.agregar_ruta_bidireccional(origen, destino, tiempo)
            print(f"  {grafo.obtener_nombre(origen)} <-> {grafo.obtener_nombre(destino)}: {tiempo} min")
        else:
            grafo.agregar_ruta(origen, destino, tiempo)
            print(f"  {grafo.obtener_nombre(origen)} -> {grafo.obtener_nombre(destino)}: {tiempo} min (solo ida)")
    
    distancias, predecesores = grafo.dijkstra(0)
    grafo.mostrar_resultados(0, distancias, predecesores)


if __name__ == "__main__":
    main()
    ejemplo_con_rutas_dirigidas()
