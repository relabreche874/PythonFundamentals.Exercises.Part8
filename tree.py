import os

file_path = '/Users/robert/Desktop/PythonProjects/PyFun8'

def directory_reader(dir):
    file_names = os.listdir(dir)
    for file in file_names:
        print(file)
        print(os.path.abspath(os.path.join(dir, file)))


if __name__ == '__main__':
    directory_reader(file_path)