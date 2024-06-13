import setuptools

setuptools.setup(
    name='mockai',
    packages=find_packages(include=['mockai']),
    version='0.1.0',
    description='Simulates the use of cloud-based API models.',
    long_description='A Python library which simulates the use of cloud-based API models for educational purposes.',
    author='Boris Ruf',
    url='https://github.com/borisruf/mockai',
    install_requires=[
        'random',
        'time',
        'difflib',
        'pickle',
        'warnings'
    ]
)