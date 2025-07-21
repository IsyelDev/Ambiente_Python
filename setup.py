from setuptools import setup
from struct import pack

setup(
    name="paquetes",
    version="1.1",
    description="Un paquete de saludar y Despedida",
    author="EMDT",
    author_email="delap@gmail.com",
    url="https://www.google.com",
    packages=["paquetes","paquetes.adios","paquetes.saludos"],
    scripts=["test.py"]
)

# Run en este archivo python3 setup.py sdist
# pip install paquetes-2.0.tar.gz --upgrade