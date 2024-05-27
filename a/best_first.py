import time

# =========================================================
# Implementaciones relacionadas al algoritmo Primero por lo Mejor
# =========================================================

def best_first(start_node, goal_node):
    current = (None, None, None) # Tupla encargada de llevar registro del nodo actual (1), nodo desde el que se llegó (2), y costo (3)
    open = [] # Lista de tuplas encargada de llevar registro de la lista Abiertos. Nodo (1), nodo desde el que se llegó (2), y costo (3)
    closed = [] # Lista de tuplas encargada de llevar registro de la lista Cerrados. Nodo (1), nodo desde el que se llegó (2), y costo (3)
    path = []

    print()
    print("Actual: -")
    print(f"Abiertos: [{start_node.name}_{start_node.name}: {straight_line_distance[start_node.name, start_node.name]}]")
    print("Cerrados: []")

    new_tuple = (start_node, start_node, straight_line_distance[start_node.name, start_node.name])
    open.append(new_tuple)

    while current[0] is not goal_node:
        open_lowest = open.pop(get_lowest_tuple_index(open))
        current = (open_lowest[0], open_lowest[1], open_lowest[2])

        for neighbor in current[0].neighbors:
            # Si el nodo no ha sido cerrado, se crea otra tupla y se añade a Abiertos
            if not node_is_in_closed(neighbor, closed):
                new_tuple = (neighbor, current[0], straight_line_distance[neighbor.name, current[0].name]+current[2])
                open.append(new_tuple)
            open = clean_open_from_duplicates(open) # Se buscan los nodos duplicados dentro de Abiertos para dejar solo uno, el de menor costo
        
        closed.append(current)
        print_step(current, open, closed)
    
    current = closed[len(closed) - 1]
    while current[0] is not start_node:
        path.append(current[0].name)

        for tuple in closed:
            if tuple[0] == current[1]:
                current = tuple
    path.append(start_node.name)
    path = path[::-1]

    print()
    print(f"El mejor camino para llegar del nodo {start_node.name} al {goal_node.name} es:")
    for i in range(len(path)):
        print(f"{path[i]}", end="" if i == len(path) - 1 else " -> ")
    print()


def get_lowest_tuple_index(tuple_array):
    lowest = float('inf')
    index_lowest = None

    for i in range(len(tuple_array)):
        # Se busca el tercer valor de las tuplas, el cual represeta el costo, para buscar el mínimo
        if tuple_array[i][2] < lowest:
            lowest = tuple_array[i][2]
            index_lowest = i
    return index_lowest


def node_is_in_closed(node_to_check, closed):
    for tuple in closed:
        if node_to_check.name == tuple[0].name:
            return True
    return False


def clean_open_from_duplicates(open):
    nodes_accounted_for = []
    clean_open = [] # Arreglo de tuplas donde se guardan los valores minimos de cada nodo

    for tuple in open:
        if tuple[0] not in nodes_accounted_for: # Si el nodo no ha sido tomado en cuenta, automáticamente se considera el menor y se mete a la lista
            nodes_accounted_for.append(tuple[0])
            clean_open.append(tuple)
        else: # Si el nodo ya está metido en la lista, significa que debe de compararse con el otro para ver cuál tiene menor peso
            print(tuple[0].name)
            for i in range(len(clean_open)): 
                for tuple_clean in clean_open:
                    if tuple_clean[0] == tuple[0] and tuple[2] < tuple_clean[2]: # Si el costo del nodo es menor al del mismo nodo ya registrado, lo reemplaza
                        print("REPLACED:",tuple_clean[0].name,tuple[0].name)
                        clean_open[i] = tuple 
                        break

    return clean_open


def print_step(current, open, closed):
    # Impimir actual
    print()
    print(f"Actual: {current[0].name}_{current[1].name}: {current[2]}")

    # Imprimir lista Abiertos
    print(f"Abiertos: [", end="")
    for tuple in open:
        print(f"{tuple[0].name}_{tuple[1].name}: {tuple[2]}", end=", ")
    print(f"]")

    # Imprimir lista Cerrados
    print(f"Cerrados: [", end="")
    for tuple in closed:
        print(f"{tuple[0].name}_{tuple[1].name}: {tuple[2]}", end=", ")
    print(f"]")


# =========================================================
# Implementaciones relacionadas a los nodos
# =========================================================


def get_node(node_list, name):
    for node in node_list:
        if node.name == name:
            return node
    return None


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def print_neighbors(self):
        print(f'Neighbors of {self.name}:')
        for neighbor in self.neighbors:
            print(f'  {neighbor.name}')
        print()


# =========================================================
# Creación del mapa de nodos y sus distancias entre sí
# =========================================================


node_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
node_list = [Node(name) for name in node_names]

node_list[0].add_neighbor(node_list[1])  # A -> B
node_list[0].add_neighbor(node_list[2])  # A -> C
node_list[0].add_neighbor(node_list[3])  # A -> D
node_list[0].add_neighbor(node_list[4])  # A -> E
node_list[0].add_neighbor(node_list[6])  # A -> G
node_list[1].add_neighbor(node_list[0])  # B -> A
node_list[1].add_neighbor(node_list[2])  # B -> C
node_list[1].add_neighbor(node_list[4])  # B -> E
node_list[1].add_neighbor(node_list[5])  # B -> F
node_list[1].add_neighbor(node_list[6])  # B -> G
node_list[1].add_neighbor(node_list[7])  # B -> H
node_list[2].add_neighbor(node_list[0])  # C -> A
node_list[2].add_neighbor(node_list[1])  # C -> B
node_list[2].add_neighbor(node_list[3])  # C -> D
node_list[2].add_neighbor(node_list[4])  # C -> E
node_list[2].add_neighbor(node_list[8])  # C -> I
node_list[3].add_neighbor(node_list[0])  # D -> A
node_list[3].add_neighbor(node_list[2])  # D -> C
node_list[3].add_neighbor(node_list[6])  # D -> G
node_list[3].add_neighbor(node_list[8])  # D -> I
node_list[3].add_neighbor(node_list[9])  # D -> J
node_list[4].add_neighbor(node_list[0])  # E -> A
node_list[4].add_neighbor(node_list[1])  # E -> B
node_list[4].add_neighbor(node_list[2])  # E -> C
node_list[4].add_neighbor(node_list[7])  # E -> H
node_list[5].add_neighbor(node_list[1])  # F -> B
node_list[5].add_neighbor(node_list[6])  # F -> G
node_list[5].add_neighbor(node_list[7])  # F -> H
node_list[6].add_neighbor(node_list[0])  # G -> A
node_list[6].add_neighbor(node_list[1])  # G -> B
node_list[6].add_neighbor(node_list[3])  # G -> D
node_list[6].add_neighbor(node_list[5])  # G -> F
node_list[6].add_neighbor(node_list[9])  # G -> J
node_list[7].add_neighbor(node_list[1])  # H -> B
node_list[7].add_neighbor(node_list[4])  # H -> E
node_list[7].add_neighbor(node_list[5])  # H -> F
node_list[8].add_neighbor(node_list[2])  # I -> C
node_list[8].add_neighbor(node_list[3])  # I -> D
node_list[8].add_neighbor(node_list[9])  # I -> J
node_list[9].add_neighbor(node_list[3])  # J -> D
node_list[9].add_neighbor(node_list[6])  # J -> G
node_list[9].add_neighbor(node_list[8])  # J -> I

straight_line_distance = {
    ('A', 'A'): 0, ('A', 'B'): 1.8, ('A', 'C'): 2.5, ('A', 'D'): 2.8, ('A', 'E'): 4.5, ('A', 'F'): 5.0,
    ('A', 'G'): 3.0, ('A', 'H'): 5.5, ('A', 'I'): 5.8, ('A', 'J'): 6.4,
    ('B', 'A'): 1.8, ('B', 'B'): 0, ('B', 'C'): 4.4, ('B', 'D'): 5.6, ('B', 'E'): 3.5, ('B', 'F'): 2.3,
    ('B', 'G'): 4.5, ('B', 'H'): 3.2, ('B', 'I'): 8.6, ('B', 'J'): 10.8,
    ('C', 'A'): 2.5, ('C', 'B'): 4.4, ('C', 'C'): 0, ('C', 'D'): 3.8, ('C', 'E'): 3.4, 
    ('C', 'F'): 8.0, ('C', 'G'): 6.3, ('C', 'H'): 7.7, ('C', 'I'): 4.0, ('C', 'J'): 9.5,
    ('D', 'A'): 2.8, ('D', 'B'): 5.6, ('D', 'C'): 3.8, ('D', 'D'): 0, ('D', 'E'): 7.7, 
    ('D', 'F'): 8.0, ('D', 'G'): 2.8, ('D', 'H'): 10.0, ('D', 'I'): 3.0, ('D', 'J'): 4.6,
    ('E', 'A'): 4.5, ('E', 'B'): 3.5, ('E', 'C'): 3.4, ('E', 'D'): 7.7, ('E', 'E'): 0, 
    ('E', 'F'): 6.7, ('E', 'G'): 6.8, ('E', 'H'): 4.0, ('E', 'I'): 8.7, ('E', 'J'): 13.5,
    ('F', 'A'): 5.0, ('F', 'B'): 2.3, ('F', 'C'): 8.0, ('F', 'D'): 8.0, ('F', 'E'): 6.7, 
    ('F', 'F'): 0, ('F', 'G'): 5.3, ('F', 'H'): 3.5, ('F', 'I'): 11.8, ('F', 'J'): 12.3,
    ('G', 'A'): 3.0, ('G', 'B'): 4.5, ('G', 'C'): 6.3, ('G', 'D'): 2.8, ('G', 'E'): 6.8, 
    ('G', 'F'): 5.3, ('G', 'G'): 0, ('G', 'H'): 6.6, ('G', 'I'): 7.5, ('G', 'J'): 6.8,
    ('H', 'A'): 5.5, ('H', 'B'): 3.2, ('H', 'C'): 7.7, ('H', 'D'): 10.0, ('H', 'E'): 4.0, 
    ('H', 'F'): 3.5, ('H', 'G'): 6.6, ('H', 'H'): 0, ('H', 'I'): 12.5, ('H', 'J'): 15.2,
    ('I', 'A'): 5.8, ('I', 'B'): 8.6, ('I', 'C'): 4.0, ('I', 'D'): 3.0, ('I', 'E'): 8.7, 
    ('I', 'F'): 11.8, ('I', 'G'): 7.5, ('I', 'H'): 12.5, ('I', 'I'): 0, ('I', 'J'): 6.4,
    ('J', 'A'): 6.4, ('J', 'B'): 10.8, ('J', 'C'): 9.5, ('J', 'D'): 4.6, ('J', 'E'): 13.5, 
    ('J', 'F'): 12.3, ('J', 'G'): 6.8, ('J', 'H'): 15.2, ('J', 'I'): 6.4, ('J', 'J'): 0
}

start_node = input("Nodo de inicio: ")
goal_node = input("Nodo meta: ")

best_first(get_node(node_list, start_node.upper()), get_node(node_list, goal_node.upper()))