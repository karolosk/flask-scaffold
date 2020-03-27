import os


def create_directories():
    
    folders_to_create = ['models', 'controllers', 'services']

    for folder in folders_to_create:
        try:
            os.mkdir(folder)
        except OSError:
            print(f'Could not create subdirectory: {folder}')
        else:
            print(f'Created subdirectory: {folder}')


def create_init_files():
    pass


def create_other_files():  
    pass