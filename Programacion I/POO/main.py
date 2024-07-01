from class_boligrafo import Bolígrafo

def mostrar_menu():
    print("\nBienvenido al menu de SmartPen:")
    print("1. Escribir con su Boligrafo")
    print("2. Recargar su Boligrafo")
    print("3. Salir de SmartPen")

def main():
    boligrafo_azul = Bolígrafo("Azul", "Fino")
    boligrafo_rojo = Bolígrafo("Rojo", "Grueso")

    boligrafos = {
        '1': boligrafo_azul,
        '2': boligrafo_rojo
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\nSeleccione que Boligrafo quiere usar:")
            print("1. Bolígrafo Azul (Fino)")
            print("2. Bolígrafo Rojo (Grueso)")
            seleccion = input("Seleccione una opción: ")
            if seleccion in boligrafos:
                texto = input("Ingrese un texto: ")
                resultado = boligrafos[seleccion].escribir(texto)
                print(f"Resultado: {resultado}")
            else:
                print("Selección no valida.")
        
        elif opcion == '2':
            print("\nSeleccione un bolígrafo:")
            print("1. Bolígrafo Azul (Fino)")
            print("2. Bolígrafo Rojo (Grueso)")
            seleccion = input("Seleccione una opción: ")
            if seleccion in boligrafos:
                cantidad = input("Ingrese la cantidad de tinta a recargar: ")
                if cantidad.isdigit():
                    cantidad = int(cantidad)
                    resultado = boligrafos[seleccion].recargar(cantidad)
                    print(f"Resultado: {resultado}")
                else:
                    print("Cantidad inválida. Debe ser un número entero.")
            else:
                print("Selección inválida.")
        
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()