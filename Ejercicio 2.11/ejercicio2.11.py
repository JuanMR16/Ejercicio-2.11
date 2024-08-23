def calcular_volumen(lado1, lado2, lado3):
    volumen = lado1 * lado2 * lado3
    return volumen

lado1 = float(input("Ingresa la longitud del Lado 1: "))
lado2 = float(input("Ingresa la longitud del Lado 2: "))
lado3 = float(input("Ingresa la longitud del Lado 3: "))

volumen = calcular_volumen(lado1, lado2, lado3)

def calcularPago(self, costoPorMetroCubico):
   volumen = calcular_volumen()
   return volumen * costoPorMetroCubico