from setuptools import setup, find_packages
from typing import List

HYPEN_E_NOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements from a requirements file

    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
          requirements= file_obj.readlines()
          requirements= [req.replace("\n", "") for req in requirements ]

          if HYPEN_E_NOT in requirements:
              requirements.remove(HYPEN_E_NOT)

    return requirements


setup(
name="Projects",
version="0.0.1",
author="DIKSHANTPATEL",
author_email="Dikshantpatel2210@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)