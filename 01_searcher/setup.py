from setuptools import setup, find_packages

setup(
   name='searcher',
   version='0.1',
   description='links searcher',
   author='Aleksandr Menshikov',
   author_email='foomail@foo.com',
   packages=find_packages(),
   install_requires=['requests', 'beautifulsoup4']
)