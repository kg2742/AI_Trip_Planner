from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    It removes any comments and empty lines.
    """

    with open('requirements.txt', 'r') as file:
        requirements = file.readlines()
    
    # Clean up the requirements list
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#') and not req.startswith('-e')]
    
    return requirements

print("Reading requirements from requirements.txt...")
requirements = get_requirements('requirements.txt') 
print(requirements)
setup(
    name='AI_Trip_Planner',
    version='0.1.0',
    author='Your Name',
    packages = find_packages(),
    install_requires=requirements
)