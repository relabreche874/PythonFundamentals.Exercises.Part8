import os

file_path = '/Users/robert/Desktop/PythonProjects/PyFun8'

def director_reader(path_name):
    path = ""
    for file_name in os.listdir(path_name):
        path += os.path.join(path_name, file_name) + "\n"
    return path

def writing_file(text):
    with open('directory.txt', 'w') as file:
        file.write(str(text))


if __name__ == '__main__':
    writing_file(director_reader(file_path))