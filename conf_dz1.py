import os
import platform
from zipfile import ZipFile

current_dir = ""

with ZipFile('dz1_folder.zip', 'r') as myzip:
    while True:
        command = input("$ ")
        if command == "ls":
            contents = [name[len(current_dir):].split("/")[0] for name in myzip.namelist() if name.startswith(current_dir) and name != current_dir]
            for item in sorted(set(contents)):
                print(item)
        elif command.startswith("cd"):
            target_dir = command.split(maxsplit=1)[1]
            target_path = current_dir + target_dir + "/"
            if any(name.startswith(target_path) for name in myzip.namelist()):
                current_dir = target_path
        elif command == "pwd":
            print(os.getcwd() + current_dir)
        elif command == "uname":
            print(platform.uname())
        elif command.startswith("cat"):
            file_path = current_dir + command.split(maxsplit=1)[1]
            if file_path in myzip.namelist():
                with myzip.open(file_path) as file:
                    print(file.read().decode('utf-8'))
        elif command == "exit":
            break

