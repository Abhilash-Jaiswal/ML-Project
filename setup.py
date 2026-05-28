from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str) -> List[str]:
    '''This function reads the requirements from a file 
    and returns a list of requirements.'''
    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj :
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements
    

setup(
    name='ML-Project',   
    version='0.0.1',
    author='Abhilash Jaiswal',
    author_email='abhilashaj2503@gmail.com',
    description='A machine learning project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


# setup.py is a Python configuration file used to package,
# install, and manage dependencies of a Machine Learning
# project. It helps convert the project into an installable
# Python package and simplifies deployment and code reuse.