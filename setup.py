from setuptools import setup, find_packages

setup(
    name='graph_users_groups',
    version='1.5.3',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'requests',
        'graph_headers @ git+https://unionhomemortgage.visualstudio.com/Infrastructure/_git/MODULE-Graph-Headers'
    ]
)