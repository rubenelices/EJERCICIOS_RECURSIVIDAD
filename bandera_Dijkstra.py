class Fichas:
    def __init__(self):
        self.fichas = []

    def pedir_fichas(self):
        num_fichas = int(input("Ingrese el número de fichas en la bandera: "))
        for i in range(num_fichas):
            color = input(f"Ingrese el color de la ficha {i+1}: ").lower()
            self.fichas.append(color)
    def ordenar_fichas(self):
        # Contar la frecuencia de cada color
        frecuencia = {'rojo': 0, 'verde': 0, 'azul': 0}
        for ficha in self.fichas:
            if ficha == 'rojo':
                frecuencia['rojo'] += 1
            elif ficha == 'verde':
                frecuencia['verde'] += 1
            elif ficha == 'azul':
                frecuencia['azul'] += 1

        # Generar la secuencia ordenada de fichas
        orden = []
        for color, cantidad in frecuencia.items():
            orden.extend([color] * cantidad)

        return orden

ordenador_fichas = Fichas()
ordenador_fichas.pedir_fichas()
fichas_ordenadas = ordenador_fichas.ordenar_fichas()
print(f"Fichas ordenadas: {fichas_ordenadas}")

