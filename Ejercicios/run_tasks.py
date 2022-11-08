from matriz_celery import execute
import click
import const as cs

@click.command()
@click.option('-p', '--path', prompt='Enter path', type=str, help=(cs.PATH_ARG_HELP))
@click.option('-c', '--calculate', prompt='Type of Concurrency', help=(cs.OP_ARG_HELP))
def main(path, calculate):
    execute(path, calculate)