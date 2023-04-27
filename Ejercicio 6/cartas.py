import random

palos = ["Picas", "Corazones", "Diamantes", "Treboles"]

# Generar las cartas de forma aleatoria con la funcion shuffle de la libreria random y programacion orientada a objetos

class Carta:
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero
    
    def __repr__(self):
        return f"{self.numero} de {self.palo}"
    
    def __str__(self):
        return f"{self.numero} de {self.palo}"

    def generar_cartas():
        cartas = []
        for palo in palos:
            for i in range(1, 14):
                cartas.append((palo, i))
        random.shuffle(cartas)
        return cartas

# Con la estructura de datos de arbol binario de busqueda separar las cartas en los palos correspondientes

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Arbol:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, node):
        if data[1] < node.data[1]:
            if node.left == None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        elif data[1] > node.data[1]:
            if node.right == None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)
        else:
            print("El valor ya existe en el arbol")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node != None:
            self._print_tree(node.left)
            print(str(node.data) + ' ')
            self._print_tree(node.right)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0
    
    def _height(self, node, height):
        if node == None:
            return height
        left_height = self._height(node.left, height + 1)
        right_height = self._height(node.right, height + 1)
        return max(left_height, right_height)
    
    def search(self, data):
        if self.root != None:
            return self._search(data, self.root)
        else:
            return False

    def _search(self, data, node):
        if data == node.data:
            return True
        elif data < node.data:
            if node.left == None:
                return False
            else:
                return self._search(data, node.left)
        else:
            if node.right == None:
                return False
            else:
                return self._search(data, node.right)

# Separar las cartas en los palos correspondientes
def separar_cartas(arbol):
    picas = []
    corazones = []
    diamantes = []
    treboles = []
    for carta in cartas:
        if arbol.search(carta):
            if carta[0] == "Picas":
                picas.append(carta)
            elif carta[0] == "Corazones":
                corazones.append(carta)
            elif carta[0] == "Diamantes":
                diamantes.append(carta)
            else:
                treboles.append(carta)
    return picas, corazones, diamantes, treboles

# Ordenar las cartas de cada palo de forma creciente

def ordenar_cartas_de_cada_palo_de_forma_creciente_(cartas):
    cartas.sort(key=lambda x: x[1])
    return cartas



if __name__ == "__main__":

# Generar las cartas de forma aleatoria
    cartas = Carta.generar_cartas()

# Generar el arbol binario de busqueda
    arbol = Arbol()

# Insertar las cartas en el arbol
    for carta in cartas:
        arbol.insert(carta)

    picas, corazones, diamantes, treboles = separar_cartas(arbol)

    picas = ordenar_cartas_de_cada_palo_de_forma_creciente_(picas)
    corazones = ordenar_cartas_de_cada_palo_de_forma_creciente_(corazones)
    diamantes = ordenar_cartas_de_cada_palo_de_forma_creciente_(diamantes)
    treboles = ordenar_cartas_de_cada_palo_de_forma_creciente_(treboles)

    print("Picas: ", picas)
    print("Corazones: ", corazones)
    print("Diamantes: ", diamantes)
    print("Treboles: ", treboles)






    






    
