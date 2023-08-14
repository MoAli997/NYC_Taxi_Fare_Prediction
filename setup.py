from setuptools import find_packages,setup
from typing import List

CONST = "-e ."

def get_requirements (file_path:str)-> List[str]:
    '''
    This function will return the list of requirements 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if CONST in requirements:
            requirements.remove(CONST)

    return requirements

setup(
    name = "NYC Taxi Fare Prediction", 
    version = "0.0.1",
    author = "Mohamed Soliman",
    author_email = "msoliman9723@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("Requirements.txt")
)