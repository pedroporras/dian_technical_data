from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.0'
DESCRIPTION = 'Modulo con definiciones de la DIAN'
LONG_DESCRIPTION = 'Paquete de python para manejar la informacion de los anexos tecnicos de la DIAN en Colombia'

PACKAGE_NAME = "Docedian"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url='',
    author='Pedro Porras',
    author_email='<pedroporras@inexpresivo.com>',
    keywords=['DIAN', 'Colombia'],
    license='LGPL',
    packages=find_packages(),
)
