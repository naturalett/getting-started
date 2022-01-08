from setuptools import setup
import os

setup(
    name="example-pkg-naturalett",  # Replace with your own username
    version=os.environ.get("BUILD_VERSION"),
    packages=['devopstool'],
    # scripts=['resources/'],
    install_requires=['click'],
    entry_points={'console_scripts': ['internalTool = devopstool.cli:cli']}
)


# https://github.com/cdeil/python-cli-examples/blob/master/click/greet/cli.py
# https://github.com/HariSekhon/DevOps-Bash-tools
# https://click.palletsprojects.com/en/8.0.x/quickstart/#virtualenv