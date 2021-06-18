#CLIENTS/COMMANDS.PY
import click

from clients.service import ClientService
from clients.models import Client

@click.group()#Convierte a clients en otro decorador
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The client name') # Pide imput al usuario
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    client = Client(name, company, email, position) #Inicializacion de client de Tipo Client
    client_service = ClientService(ctx.obj['clients_table']) #Inicializacion de client_service de Tipo ClientService 
    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])

    clients_list = client_service.list_clients()

    click.echo('ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION')
    click.echo ('*' * 35)

    for client in clients_list:
        click.echo('{uid} | {name} | {company} | {position}'.format(
            uid = client['uid'],
            name = client['name'],
            company = client['company'],
            position = client['position']))


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()

    client = [client for clients in client_list if client['uid'] == client_uid]

    if client: 
        client = _update_client_flow(Client(**client[0])) #en nuevo Client desempaquetamos el cliente encotrado
        client_service.update_client(client)

        click.echo('Cliente actualizado :)')
    else:
        click.echo('Cliente no encontrado')


def _update_client_flow(client):
    click.echo('Dejar vacio si no quieres modificar el valor')

    client.name = click.prompt('Nuevo nombre', type=str, default = client.name)
    client.company = click.prompt('Nueva compania', type=str, default = client.company) 
    client.email = click.prompt('Nuevo email', type=str, default = client.email) 
    client.position = click.prompt('Nueva posicion', type=str, default = client.position) 

    return client


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass


all = clients

