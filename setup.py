from setuptools import find_packages, setup

setup(
    name='mockai',
    packages=find_packages(),
    package_data={'mockai': ['cache.pickle']},
    version='0.1.0',
    description='Simulates the use of cloud-based API models.',
    long_description='A Python library which simulates the use of cloud-based API models for educational purposes.',
    author='Boris Ruf',
    url='https://github.com/borisruf/mockai'
)