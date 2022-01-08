import click
import subprocess


@click.command()
@click.option('--count', default=1, help='number of iteration')
@click.argument('repo')
def dockerhub_list_tags(count, repo):
    """List tags in DockerHub"""
    rc = subprocess.call(["./resources/dockerhub_list_tags.sh", repo])
    print(f'dockerhub_list_tags.sh')


@click.command()
@click.option('--yes', is_flag=True,
              expose_value=False,
              prompt='Are you sure you want to drop the db?')
def dropdb():
    click.echo('Dropped all tables!')
