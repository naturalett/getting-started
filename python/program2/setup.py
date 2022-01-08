import setuptools, os

setuptools.setup(
    name="example-pkg-naturalett",  # Replace with your own PyPi
    version=os.environ.get("BUILD_VERSION"),
    author="Foo Bar",
    author_email="lidor.ettinger@example.com",
    description="A small example package",
    url="https://github.com/naturalett/getting-started",
    packages=['calculate'],
    scripts=['calculate/calculate.py'],
    python_requires='>=3.9',
)
