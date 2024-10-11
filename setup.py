from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str)->List[str]: #filepath will be a string, this function will return a list 
    # ths function will return the list of requirements
    requirements = [] # initalise requirements
    with open(file_path) as file_obj: # open the file path as a temp obj named file_obj
        requirements = file_obj.readlines() # every line is added to requirement as an object of list like [pandas\n,numpyy\n,seaborn\n]
        [req.replace('\n','') for req in requirements] # remove the \n for each item and replace it with blank

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
        

    


setup(
name = 'mlproject',
version= '0.0.1',
author = 'Ahmed',
author_email= 'ahmeddaudawan70@gmail.com',
packages = find_packages(),
install_requires= get_requirements('requirements.txt')

)