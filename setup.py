from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name='duplicador',
    version='0.1.0',
    packages=find_packages(),
    description='Pacote simples para duplicar valores de uma lista',
    author='Michael Santos',
    author_email='mackellmichael@hotmail.com',
    license='MIT',
)
