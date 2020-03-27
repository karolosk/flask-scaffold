from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='flaskscaffold',
      version='0.3',
      description='Initializing project structure for flask applications.',
      url='https://github.com/karolosk/flask-scaffold',
      author='KarolosK',
      author_email='karolos.koutsoulelos@gmail.com',
      license='MIT',
      packages=['flaskscaffold'],
      zip_safe=False,
      include_package_data=True,
      scripts=['bin/flaskscaffold-create'])