from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='flaskscaffold',
      version='0.4',
      description='Initializing project structure for flask applications.',
      url='https://github.com/karolosk/flask-scaffold',
      author='KarolosK',
      author_email='karolos.koutsoulelos@gmail.com',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['flaskscaffold'],
      zip_safe=False,
      include_package_data=True,
      scripts=['bin/flaskscaffold-create'])