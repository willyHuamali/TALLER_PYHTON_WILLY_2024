"""01. Escribir un programa que pida al usuario que ingrese las calificaciones de varios
exámenes y luego calcule y muestre por pantalla el promedio de esas calificaciones."""

cantidad=int(input("Nº de calificaciones que ingresara?: "))
suma=0
i=1
while i <= cantidad:

    calificacion=float(input(f'ingrese las calificacion {i}: '))
    suma=suma+calificacion
    i += 1
promedio=round((suma/cantidad),2)
print(f'El promedio de las calificaciones es: {promedio}')
print("otra forma")


