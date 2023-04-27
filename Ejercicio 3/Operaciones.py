class Numero:
    def __init__(self, valor):
        valido = isinstance(valor, (int, float))
        if valido:
            self.valor = valor
        else:
            no_valido = valor

    def __str__(self):
        return str(self.valor) if self.valido else str(self.no_valido)

    def suma(self, otro):
        if self.valido and isinstance(otro, Numero) and otro.valido:
            return Numero(self.valor + otro.valor)
        else:
            return f"Error: Tipo de dato no válido"

    def resta(self, otro):
        if self.valido and isinstance(otro, Numero) and otro.valido:
            return Numero(self.valor - otro.valor)
        else:
            return f"Error: Tipo de dato no válido"

    def producto(self, otro):
        if self.valido and isinstance(otro, Numero) and otro.valido:
            return Numero(self.valor * otro.valor)
        else:
            return f"Error: Tipo de dato no válido"

    def division(self, otro):
        if self.valido and isinstance(otro, Numero) and otro.valido:
            if otro.valor != 0:
                return Numero(self.valor / otro.valor)
            else:
                return "Error: No es posible dividir entre cero"
        else:
            return f"Error: Tipo de dato no válido"
   