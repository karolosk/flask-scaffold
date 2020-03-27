Flask Scaffold
--------
Package to create scaffolds for flask projects.


To use simply create a directory for your project and then in the directory:

    >>> flaskscaffold-create


This will create the below folder structure:

::

    my_project
    ├── app.py
    ├── db.py
    ├── .gitignore
    ├── models         
    │   └── __init__.py
    ├── services         
    │   └── __init__.py
    ├── controllers         
    │   └── __init__.py
    ├── static
    ├── templates
    └── tests


In addition to the file structure, boilerplate app.py and .gitignore is added.