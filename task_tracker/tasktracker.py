import jsonmanager
import click
from tabulate import tabulate
from datetime import datetime

@click.group()
def cli():
    pass

#task
@cli.command()
def task():
    data = jsonmanager.read_json() 
    if len(data) <= 0:
        return f"There are currently no tasks"
    else:
        table_data = []
        table_data.append(["ID", "Description", "Status", "Created AT", "Updated At"])
        for task in data:
            each_task = [task["id"], task["description"], task["status"], task["createdAt"], task["updatedAt"]]
            table_data.append(each_task)  
        print(tabulate(table_data, headers = "firstrow", tablefmt = "fancy_grid"))  


@cli.command()
@click.argument('status', type = str)
def list(status):
    list_status = ['done', 'todo', 'in-progress']
    if status not in list_status:
        return f"Invalid argument. Usage: task done/todo/in-progress"  
    data = jsonmanager.read_json()
    if len(data) < 0:
        return f"There are no pending tasks"
    else:
        table_data = []
        table_data.append(['ID', 'Description', 'Status', 'Created At', 'Updated At'])  
        for task in data:
            if task['status'] == status:
                each_task = [task['id'], task['description'], task['status'], task['createdAt'], task['updatedAt']]
                table_data.append(each_task)
        print(tabulate(table_data, headers = "firstrow", tablefmt = "fancy-grid"))

@cli.command()
@click.argument('task', type = str)
def add(task):
    data = jsonmanager.read_json()
    newID = len(data) + 1
    now = datetime.now()
    task = {
        'id' : newID,
        'description': task,
        'status' : 'todo',
        'createdAt': now.strftime("%d/%m/%Y %H:%M:%S"),
        'updatedAt' : ''
    }
    data.append(task)
    jsonmanager.write_json(data)
    print(f"Task been successfully created (ID: {task['id']})")


#deleting task
@cli.command()
@click.argument('id', type = int)
def delete(id):
    data = jsonmanager.read_json()
    task = next((x for x in data if x['id'] == id), None)

    if task:
        data.remove(task)
        jsonmanager.write_json(data)
        print(f"Task with the ID {id} has been removed")
    else:
        print(f"Task with the ID {id} has been not found")

#updating task
@cli.command()
@click.argument('id', type = int)
@click.option('--task', required = True, help = "New task description")
def update(id, task):
    data = jsonmanager.read_json()
    item = next((t for t in data if t['id'] == id), None)
    if not item:
        print("Task with task{id} not found")
    else:
        if task is not None:
            item['description'] = task
            now = datetime.now()
            item['updatedAt'] = now.strftime("%d/%m/%Y %H:%M:%S")
        jsonmanager.write_json(data)
        print(f"Task with ID {id} has been updated")

#marking the task
@cli.command()
@click.argument('id', type = int)
def mark_in_process(id):
    data = jsonmanager.read_json()
    item = next((t for t in data if t['id'] == id), None)
    if not item:
        print(f"Task with the ID {id} not found")
    else:
        item['status'] = 'in-process'
        now = datetime.now()
        item['updatedAt'] = now.strftime("%d/%m/%Y %H:%M:%S")
    jsonmanager.write_json(data)
    print(f"The status of the task with the ID {id} has been updated")

@cli.command()
@click.argument('id', type = int)
def mark_done(id):
    data = jsonmanager.read_json()
    item = next((t for t in data if t['id'] == id), None)
    if not item:
        print(f"The task with ID {id} not found")
    else:
        item['status'] = 'done'
        now = datetime.now()
        item['updatedAt'] = now.strftime("%d/%m/%Y %H:%M:%S")
    jsonmanager.write_json(data)
    print(f"The status of the task with ID {id} has been updated")


    


if __name__ == "__main__":
    cli()
