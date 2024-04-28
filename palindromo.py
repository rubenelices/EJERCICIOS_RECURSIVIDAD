class Palindromo:
    def __init__(self, frase):
        self.frase = frase  # Inicializa el atributo con la frase proporcionada
    
    def test(self):
        # Convertir la frase a minúsculas, quitar los acentos y los espacios antes de comparar
        frase_procesada = self.remover_espacios_y_acentos(self.frase.lower())
        return frase_procesada == frase_procesada[::-1]
    
    def remover_espacios_y_acentos(self, frase):
        # Diccionario para mapear caracteres con tilde a sus equivalentes sin tilde
        acentos = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u','Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
        }
        # Remover los espacios en blanco y los acentos de la frase
        frase_sin_espacios_ni_acentos = ''.join(acentos.get(char, char) for char in frase if char != ' ')
        return frase_sin_espacios_ni_acentos
    
    def __del__(self):
        # Imprime la frase en mayúsculas al destruir la instancia
        print(self.frase.upper())

frase_usuario = input("Por favor, ingresa una frase: ")
p = Palindromo(frase_usuario)

resultado = p.test()
print(f"¿'{frase_usuario}' es un palíndromo?: {'Sí' if resultado else 'No'}")



