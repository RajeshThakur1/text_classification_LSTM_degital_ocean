from setuptools import setup, find_packages
REMOVE_PACKAGE = "-e ."
REQUIREMENT_FILE_NAME= "requirements.txt"

def get_requirement_list(requirement_file_name= REQUIREMENT_FILE_NAME) -> list:
    try:
        with open(requirement_file_name) as requirement_file:
            requirement_list = [requirement.replace("\n","") for requirement in requirement_file.readlines()]
            requirement_list.remove(REMOVE_PACKAGE)
        return requirement_list
    except Exception as e:
        raise e

setup(
    name= "lstm-text-classification",
    version="0.0.1",
    description= "LSTM based text classification project deploy in Degital ocean",
    author="Rajesh Thakur",
    packages=find_packages(),
    install_requires=get_requirement_list()
)