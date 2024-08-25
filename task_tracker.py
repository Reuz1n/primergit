import argparse
import json
import os

# Archivo que almacena tareas
TASKS_FILE = 'tasks.json'

# Verificar si el archivo JSON existe, si no existe lo crear
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as file:
        json.dump([], file)

def load_tasks():
    """Carga las tareas desde el archivo .JSON"""
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    """Guarda las tareas en el archivo .JSON"""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def parse_args():
    parser = argparse.ArgumentParser(description="Seguimiento de tareas")
    parser.add_argument('action', choices=['add', 'update', 'delete', 'list', 'done', 'inprogress'], help="Acción a realizar")
    parser.add_argument('params', nargs='*', help="Parámetros para la acción")
    return parser.parse_args()

def add_task(description):
    tasks = load_tasks()
    new_id = len(tasks) + 1
    new_task = {
        'id': new_id,
        'description': description,
        'status': 'not done'
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarea agregada: {new_task}")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == int(task_id):
            task['description'] = new_description
            save_tasks(tasks)
            print(f"Tarea actualizada: {task}")
            return
    print("Tarea no encontrada")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != int(task_id)]
    save_tasks(tasks)
    print(f"Tarea {task_id} eliminada")

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = 'in progress'
            save_tasks(tasks)
            print(f"Tarea marcada como en progreso: {task}")
            return
    print("Tarea no encontrada")

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = 'done'
            save_tasks(tasks)
            print(f"Tarea marcada como hecha: {task}")
            return
    print("Tarea no encontrada.")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [task for task in tasks if task['status'] == filter_status]
    for task in tasks:
        print(f"{task['id']}: {task['description']} [{task['status']}]")

if __name__ == '__main__':
    args = parse_args()
    
    if args.action == 'add':
        if args.params:
            add_task(" ".join(args.params))
        else:
            print("Error: Debes proporcionar una descripción para la tarea")
    elif args.action == 'update':
        if len(args.params) >= 2:
            update_task(args.params[0], " ".join(args.params[1:]))
        else:
            print("Error: Debes proporcionar un ID de tarea y una nueva descripción")
    elif args.action == 'delete':
        if args.params:
            delete_task(args.params[0])
        else:
            print("Error: Debes proporcionar un ID de tarea")
    elif args.action == 'list':
        list_tasks()
    elif args.action == 'done':
        if args.params:
            mark_done(args.params[0])
        else:
            print("Error: Debes proporcionar un ID de tarea")
    elif args.action == 'inprogress':
        if args.params:
            mark_in_progress(args.params[0])
        else:
            print("Error: Debes proporcionar un ID de tarea")
