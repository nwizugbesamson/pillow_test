"""
A basic cli app with click library
Click documentation: https://click.palletsprojects.com/en/8.1.x/
"""
import click


@click.group()
def cli():
    pass

@click.command()
def dropdb():
    """Just to illustrate operation that doesn't require any argument"""
    click.echo('Dropped the database')

@click.command()
@click.option('-u', '--user', prompt='Your username', help='Your username')
@click.option('-p', '--pwd', prompt='Your password', help='password.')
def startapp(user, pwd):
    """Startapp as a user"""
    click.echo('Initialized the CLI')
    click.echo(f"Logged in as {user}!")

@click.command()
@click.option('-a', '--avatar', prompt='Your avatar', help='Your avatar')
@click.option('-n', '--name', prompt='Your name', help='The person to greet.')
def register(avatar, name):
    """Register Avatar"""
    click.echo(f"Hello {name} with {avatar} avatar!")

@click.command()
@click.option('-c', '--color', prompt='Your complexion', help='Your complexion')
@click.option('-s', '--sex', prompt='Your sex', help='Your sex')
def add_bio(color, sex):
    """Add Bio"""
    click.echo(f"Bio: {color} {sex}!")

# registering the commands
if __name__=='__main__':
    cli.add_command(startapp)
    cli.add_command(dropdb)
    cli.add_command(register)
    cli.add_command(add_bio)
    cli()