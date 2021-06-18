#PV.PY
import click

from clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'


@click.group() #Decorador apuntando al punto de entrada
@click.pass_context #Decorador que nos da el objeto contexto
def cli(ctx): #Punto de entrada
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(clients_commands.all) #all es una variable en clients/commands que apunta a las funciones de clients
