tareas = []

def mostrar_menu():
    print("\nGestor de Tareas")
    print("1. Mostrar la lista de tareas")
    print("2. Agregar una tarea")
    print("3. Eliminar una tarea")
    print("4. Salir")

def mostrar_tareas():
    if not tareas:
        print("\nLa lista de tareas está vacía.")
    else:
        print("\nLista de tareas:")
        for idx, tarea in enumerate(tareas, start=1):
            print(f"{idx}. {tarea}")

def agregar_tarea():
    tarea = input("\nEscribe la nueva tarea: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada a la lista.")

def eliminar_tarea():
    mostrar_tareas()
    if tareas:
        try:
            indice = int(input("\nEscribe el número de la tarea que deseas eliminar: "))
            if 1 <= indice <= len(tareas):
                tarea_eliminada = tareas.pop(indice - 1)
                print(f"Tarea '{tarea_eliminada}' eliminada de la lista.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")
        if opcion == '1':
            mostrar_tareas()
        elif opcion == '2':
            agregar_tarea()
        elif opcion == '3':
            eliminar_tarea()
        elif opcion == '4':
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()