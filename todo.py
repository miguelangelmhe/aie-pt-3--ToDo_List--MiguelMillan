import csv
import os

TODOS_FILE = "todos.csv"

todos = []


def add_one_task(title):
    todos.append(title)


def print_list():
    if not todos:
        print("No hay tareas pendientes.")
        return
    for index, task in enumerate(todos, start=1):
        print(f"{index}. {task}")


def delete_task(number_to_delete):
    index = number_to_delete - 1
    if index < 0 or index >= len(todos):
        print("Numero de tarea invalido.")
        return
    removed = todos.pop(index)
    print(f"Tarea eliminada: {removed}")


def save_todos():
    with open(TODOS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for task in todos:
            writer.writerow([task])


def load_todos():
    todos.clear()
    if not os.path.exists(TODOS_FILE):
        return
    with open(TODOS_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                todos.append(row[0])


def print_menu():
    print("\n=== Lista de Tareas ===")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Guardar tareas")
    print("5. Cargar tareas")
    print("6. Salir")


def main():
    load_todos()
    while True:
        print_menu()
        choice = input("Elige una opcion: ").strip()

        if choice == "1":
            title = input("Titulo de la tarea: ").strip()
            if title:
                add_one_task(title)
                print("Tarea agregada.")
            else:
                print("El titulo no puede estar vacio.")
        elif choice == "2":
            print_list()
        elif choice == "3":
            print_list()
            if todos:
                try:
                    number = int(input("Numero de tarea a eliminar: ").strip())
                    delete_task(number)
                except ValueError:
                    print("Debes ingresar un numero valido.")
        elif choice == "4":
            save_todos()
            print(f"Tareas guardadas en {TODOS_FILE}.")
        elif choice == "5":
            load_todos()
            print("Tareas cargadas.")
        elif choice == "6":
            save_todos()
            print("Hasta luego!")
            break
        else:
            print("Opcion invalida, intenta de nuevo.")


if __name__ == "__main__":
    main()
