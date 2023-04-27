from random import randint

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
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
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
        elif data < node.data and node.left != None:
            return self._search(data, node.left)
        elif data > node.data and node.right != None:
            return self._search(data, node.right)
        return False
    
    def find(self, data):
        if self.root != None:
            return self._find(data, self.root)
        else:
            return None
    
    def _find(self, data, node):
        if data == node.data:
            return node
        elif data < node.data and node.left != None:
            return self._find(data, node.left)
        elif data > node.data and node.right != None:
            return self._find(data, node.right)
    
    def delete_value(self, data):
        return self.delete_node(self.find(data))
    
    def delete_node(self, node):
        if node == None or self.find(node.data) == None:
            print("No se puede eliminar el nodo")
            return None
        
        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
        
        def num_children(n):
            num_children = 0
            if n.left != None:
                num_children += 1
            if n.right != None:
                num_children += 1
            return num_children
        
        node_parent = node.parent
        node_children = num_children(node)

        if node_children == 0:
            if node_parent != None:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None
        
        if node_children == 1:
            if node.left != None:
                child = node.left
            else:
                child = node.right
            
            if node_parent != None:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child
            
            child.parent = node_parent
        
        if node_children == 2:
            successor = min_value_node(node.right)
            node.data = successor.data
            self.delete_node(successor)

    def count_ocurrencies(self, data):
        if self.root != None:
            return self._count_ocurrencies(data, self.root)
        else:
            return 0
        
    def _count_ocurrencies(self, data, node):
        if node == None:
            return 0
        if node.data == data:
            return 1 + self._count_ocurrencies(data, node.left) + self._count_ocurrencies(data, node.right)
        else:
            return self._count_ocurrencies(data, node.left) + self._count_ocurrencies(data, node.right)

    def inorder(self):
        if self.root != None:
            self._inorder(self.root)

    def _inorder(self, node):
        if node != None:
            self._inorder(node.left)
            print(str(node.data) + ' ')
            self._inorder(node.right)

    def preorder(self):
        if self.root != None:
            self._preorder(self.root)

    def _preorder(self, node):
        if node != None:
            print(str(node.data) + ' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        if self.root != None:
            self._postorder(self.root)

    def _postorder(self, node):
        if node != None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(str(node.data) + ' ')

def fill_tree(tree, num_elems = 100, max_int = 1000):
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

def count_num_arbol(tree):
    if tree.root != None:
        return _count_num_pares_arbol(tree.root)
    else:
        return _count_num_impares_arbol(tree.root)
    
def _count_num_pares_arbol(node):
    if node == None:
        return 0
    if node.data % 2 == 0:
        return 1 + _count_num_pares_arbol(node.left) + _count_num_pares_arbol(node.right)
    else:
        return _count_num_pares_arbol(node.left) + _count_num_pares_arbol(node.right)
    
def _count_num_impares_arbol(node):
    if node == None:
        return 0
    if node.data % 2 != 0:
        return 1 + _count_num_impares_arbol(node.left) + _count_num_impares_arbol(node.right)
    else:
        return _count_num_impares_arbol(node.left) + _count_num_impares_arbol(node.right)

if __name__ == "__main__":

    tree = Arbol()
    tree = fill_tree(tree)

    tree.print_tree()
    print("Altura del arbol: " + str(tree.height()))
    print(tree.search(10))
    print(tree.search(999))
    print(tree.find(10))
    print(tree.find(999))
    print(tree.delete_value(15))
    print(tree.delete_value(14))
    print(tree.delete_value(10))
    print(tree.height())
    print(tree.count_ocurrencies(10))
    tree.print_tree()
    tree.inorder()
    tree.preorder()
    tree.postorder()
    print(count_num_arbol(tree))
