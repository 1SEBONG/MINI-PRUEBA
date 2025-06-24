import os
os.system("cls")

nombre = ""
listaNombre = [] 

while True:

    while True:
        print ("1.- Agregar alumnos")
        print ("2.- Mostrar todos los alumnos")
        print ("3.- Salir")

        try:
            opcion = int(input("\nIngrese su eleccion (1/2/3): "))
            if (1 <= opcion and opcion <=3):
                break
            else:
                print("Por favor seleccione las opciones mostradas (1/2/3).")
        except ValueError:
            print("ERROR. Ingrese un dato valido de numero entero (1/2/3).")
    
    if opcion == 1:
        nombre = input("\nIngrese su nombre: ")
        print("Su nombre se ingreso correctamente.")
        listaNombre.append(nombre)


    if opcion == 2:
        print (listaNombre)

    if opcion == 3:
        break