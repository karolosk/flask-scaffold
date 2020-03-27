import os
from .create_scaffold import create_directories, create_init_files, create_other_files

def test():
    print('hello')

def create():
    
    path = os.getcwd()
    print(f'Working directory: {path}')

    create_directories()
   

def insteall_dependencies():
    pass
