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
    
    
def main():
    pass