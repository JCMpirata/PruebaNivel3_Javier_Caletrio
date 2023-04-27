class Nodo:
    def __init__(self, nombre, multiverso, mision):
        self.nombre = nombre
        self.multiverso = multiverso
        self.mision = mision
        self.rama_si = None
        self.rama_no = None

    def prioridad(self):
        if self.nombre == "Gran Conquistador" or self.multiverso == "616" or self.mision == "El que permanece":
            return 1
        elif self.nombre == "Khan que todo lo sabe" or self.multiverso == "838" or self.mision == "Carnicero de Dioses":
            return 2
        else:
            return 3
        
bitacora = []
        
def pedido(nombre, multiverso, mision):
    pedir = Nodo(nombre, multiverso, mision)
    prioridad = pedir.prioridad()
    if prioridad == 1:
        bitacora.insert(0, pedir)
    elif prioridad == 2:
        bitacora.insert(len(bitacora)//2, pedir)   
    else:
        bitacora.append(pedir)

def mostrar_bitacora():
    if bitacora:
        pedidos = bitacora.pop(0)
        print("Nombre: ", pedidos.nombre, "Multiverso: ", pedidos.multiverso, "Mision: ", pedidos.mision)
        mostrar_bitacora()
    else:
        print("No hay mas pedidos")

if __name__ == "__main__":
    pedido("Khan que todo lo sabe", "838", "Carnicero de Dioses")
    pedido("Gran Conquistador", "616", "El que permanece")
    pedido("Thanos", "1", "Destruir la mitad del universo con las gemas del infinito")

    mostrar_bitacora()

    








