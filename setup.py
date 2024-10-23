from setuptools import find_packages, setup
from typing import List


HYPEN = '-e .'
def get_requirements(file_path:str)->List[str]:
  """This function will return the list of requirments"""
  requirements = []
  with open(file_path) as file_obj: #temporary file object
    requirements = file_obj.readlines()
    [req.replace("\n", "") for req in requirements]
    
    if HYPEN in requirements:
      requirements.remove(HYPEN)
      
    return requirements




setup(
  name= 'genericmlproject',
  version='0.0.1',
  author='Muavia',
  author_email='muaviashakeel70@gmail.com',
  packages=find_packages(),
  install_requires= get_requirements('requirements.txt')
)
