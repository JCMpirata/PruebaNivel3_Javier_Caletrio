class Nodo:
    def __init__(self, pregunta, rama_si, rama_no):
        self.pregunta = pregunta
        self.rama_si = rama_si
        self.rama_no = rama_no

    def tomar_decision(self):
        respuesta = input(self.pregunta)
        if respuesta == "si":
            self.rama_si.tomar_decision()
        elif respuesta == "no":
            self.rama_no.tomar_decision()
        else:
            print("Respuesta no valida")
            self.tomar_decision()

if __name__ == "__main__":

    nodo_pregunta1 = Nodo("¿La mision es intergalactica?", None, None)
    nodo_pregunta2 = Nodo("¿La mision es de recuperacion y no se puede ser detectado?", None, None)
    nodo_pregunta3 = Nodo("¿La mision es de destruccion?", None, None)
    nodo_pregunta4 = Nodo("¿Se necesita rescatar alguna persona?", None, None)
    nodo_pregunta5 = Nodo("¿Se necesita viajar entre galaxias?", None, None)
    nodo_pregunta6 = Nodo("¿Hay que infiltrarse en algun lugar?", None, None)
    nodo_pregunta7 = Nodo("¿Es Nick Fury el solicitante?", None, None)
    nodo_pregunta8 = Nodo("¿Se necesita destruir un ejercito completo?", None, None)

    nodo_resultado1 = Nodo("Kahn", None, None)
    nodo_resultado2 = Nodo("Antman", None, None)
    nodo_resultado3 = Nodo("Hulk", None, None)
    nodo_resultado4 = Nodo("Capitan America", None, None)
    nodo_resultado5 = Nodo("Capitana Marvel", None, None)
    nodo_resultado6 = Nodo("Winter Soldier", None, None)
    nodo_resultado7 = Nodo("Nick Fury", None, None)
    nodo_resultado8 = Nodo("Thor", None, None)


    nodo_pregunta1.rama_si = nodo_pregunta2
    nodo_pregunta1.rama_no = nodo_resultado2
    nodo_pregunta2.rama_si = nodo_resultado1
    nodo_pregunta2.rama_no = nodo_pregunta3
    nodo_pregunta3.rama_si = nodo_resultado2
    nodo_pregunta3.rama_no = nodo_resultado1

    nodo_pregunta1.tomar_decision()



    


    





