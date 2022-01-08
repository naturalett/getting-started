import click
import subprocess
# from .dockerhub_list_tags import dockerhub_list_tags


@click.group()
def cli():
    """Command line interface"""
    pass

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

@click.command()
@click.option("--cloud", default="AWS")
def authentication(cloud):
    click.echo(f"Authorizing to the cloud, {cloud}!")

cli.add_command(dockerhub_list_tags)
cli.add_command(dropdb)
cli.add_command(authentication)

if __name__ == '__main__':
    cli()
