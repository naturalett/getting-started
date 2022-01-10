from setuptools import setup
import os

setup(
    name="devopstoolscli",  # Replace with your own username
    version="1.1",
    packages=['devopstool'],
    # scripts=['resources/*'],
    install_requires=['click'],
    entry_points={'console_scripts': ['internalTool = devopstool.cli:cli']}
)
