from setuptools import find_packages,setup
from typing import List
hy='-e .'
def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path) as fil:
        requirements=fil.readlines()
        requirements=[req.replace("/n"," ") for req in requirements]
        if hy in requirements:
            requirements.remove(hy)
    return requirements        


setup(
    name='ML project',
    version='0.0.1',
    author='Likhita',
    author_email='chillalikhita1242@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)