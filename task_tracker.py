import json
import os
import argparse  #libreria nazi para terminal(leer documentacion)


# nombre del .json
tasks_file = 'tasks.json'

# Ve si tasks.json existe
if not os.path.exists(tasks_file):
    with open(tasks_file, 'w') as file:
        json.dump([], file)

# Carga .json
def carga_tasks():
    with open(tasks_file, 'r') as file:
        return json.load(file)
    
# guarda las tareas en  .json
def guarda_tasks(tasks):
    with open(tasks_file, 'w') as file:
        json.dump(tasks, file, indent=4)

