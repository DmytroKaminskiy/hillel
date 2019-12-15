import os


def read_requirements():
    req_path = os.path.join(os.getcwd(), 'requirements.txt')
    with open(req_path) as file:
        return file.read()
