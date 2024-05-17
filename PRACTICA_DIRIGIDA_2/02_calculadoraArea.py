"""2. Escribir un programa que pregunte al usuario las dimensiones de un rectángulo (largo y ancho) 
y calcule tanto el área como el perímetro del rectángulo, mostrando ambos valores por pantalla."""

def main():
   largo = int(input("Ingrese el largo: "))
   ancho = int(input("Ingrese el ancho: "))
   area = largo * ancho
   perimetro = 2 * (largo + ancho)
   print("El area es: ", area)
   print("El perimetro es: ", perimetro)

if __name__ == "__main__":
    main()  