from setuptools import find_packages, setup
from typing import List

def get_requirements(): #this function will return list of requirements
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Aanushka Saha",
    author_email="sahaaanushka28@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
