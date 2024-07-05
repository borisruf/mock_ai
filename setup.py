from setuptools import find_packages, setup

VERSION = '0.0.1'

setup(
    name='stub_ai',
    version=VERSION,
    packages=find_packages(),
    package_data={'stub_ai': ['cache.pickle']},
    install_requires=['openai'],
    description='Simulates the use of cloud-based API models.',
    long_description='A Python library which simulates the use of cloud-based AI models for educational purposes.',
    author='Boris Ruf',
    url='https://github.com/borisruf/stub_ai'
)