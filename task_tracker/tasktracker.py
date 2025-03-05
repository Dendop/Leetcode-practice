import sys
import json
import argparse
from tabulate import tabulate
from datetime import datetime

def add(string):
    #add task
    pass
def delete(string):
    pass
def update(string):
    pass
def print_tasks(string):
    pass
def mark(string):
    pass

def main():

        try:
            some_task = sys.argv[1].lower()
            supported_functions = {
                "add": add,
                "delete" : delete,
                "update" : update,
                "list" : print_tasks,
                "mark" : mark
            }
            valid_commands = ["add", "delete", "update","list", "mark"]
            if some_task not in valid_commands:
                raise ValueError("Invalid command. Expected: add 'task', delete 'task', update 'task', list 'done'/'not done'/'in progress'")

            supported_functions[some_task](sys.argv[2])
            some_time = datetime.now()
            print(some_time)

        except ValueError as e:
            print(e)
if __name__ == "__main__":
    main()