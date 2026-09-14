# aie-pt-3--ToDo_List--MiguelMillan

Lista de tareas CLI en Python, pensada para registrar, consultar y eliminar tareas pendientes desde la terminal, guardando el progreso en `todos.csv`.

## Requisitos

- Python 3 (solo librería estándar, sin dependencias externas).

## Cómo lanzarlo

Desde la raíz del repositorio, ejecuta:

```bash
python3 todo.py
```

Al iniciar, la aplicación carga automáticamente las tareas guardadas en `todos.csv` (si el archivo existe) y muestra un menú interactivo con las siguientes opciones:

1. Agregar tarea
2. Mostrar tareas
3. Eliminar tarea
4. Guardar tareas
5. Cargar tareas
6. Salir (guarda automáticamente antes de cerrar)

Puedes agregar tantas tareas como necesites dentro de la misma ejecución antes de guardar o salir.