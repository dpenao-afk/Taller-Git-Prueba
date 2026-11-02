class Grafo:
    def __init__(self):
        # Operación básica: Inicializar la lista de adyacencia
        self.lista_adyacencia = {}

    def insertar_vertice(self, vertice):
        """Operación básica: Añadir un nuevo nodo al grafo"""
        if vertice not in self.lista_adyacencia:
            self.lista_adyacencia[vertice] = []
            print(f"Vértice '{vertice}' insertado con éxito.")
        else:
            print(f"El vértice '{vertice}' ya existe.")

    def insertar_arista(self, desde_nodo, hacia_nodo, bidireccional=True):
        """Operación básica: Crear una conexión entre dos nodos"""
        # Asegurar que ambos vértices existan antes de conectarlos
        if desde_nodo not in self.lista_adyacencia:
            self.insertar_vertice(desde_nodo)
        if hacia_nodo not in self.lista_adyacencia:
            self.insertar_vertice(hacia_nodo)
        
        # Añadir la conexión
        if hacia_nodo not in self.lista_adyacencia[desde_nodo]:
            self.lista_adyacencia[desde_nodo].append(hacia_nodo)
            
        # Si es un grafo no dirigido, añadimos la conexión inversa
        if bidireccional and desde_nodo not in self.lista_adyacencia[hacia_nodo]:
            self.lista_adyacencia[hacia_nodo].append(desde_nodo)
        
        print(f"Arista creada entre '{desde_nodo}' y '{hacia_nodo}'.")

    def mostrar_grafo(self):
        """Operación básica: Visualizar la estructura actual del grafo"""
        print("\n--- Estructura del Grafo (Lista de Adyacencia) ---")
        for vertice, vecinos in self.lista_adyacencia.items():
            print(f"Vértice {vertice} -> Conectado con: {', '.join(map(str, vecinos)) if vecinos else 'Ninguno'}")


# --- PRUEBA DE LAS OPERACIONES BÁSICAS ---
if __name__ == "__main__":
    mi_grafo = Grafo()
    
    # 1. Insertar vértices
    mi_grafo.insertar_vertice("A")
    mi_grafo.insertar_vertice("B")
    mi_grafo.insertar_vertice("C")
    
    # 2. Insertar aristas (conexiones)
    mi_grafo.insertar_arista("A", "B")
    mi_grafo.insertar_arista("A", "C")
    mi_grafo.insertar_arista("B", "D")  # Inserta 'D' automáticamente al conectar
    
    # 3. Mostrar el estado final del grafo
    mi_grafo.mostrar_grafo()
