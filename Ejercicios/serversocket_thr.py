import click
import const as cs
import subprocess


@click.command()
@click.option('--command', prompt='Enter command',
            help='The command to execute.')
# @click.option('--count', prompt='Count', type=int, help='Number of greetings.')

def execute(command):
    p = subprocess.Popen(command)
    click.echo(p)

if __name__ == '__main__':
    execute()