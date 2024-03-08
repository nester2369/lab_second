import os

dir_name = input("Введите название новой директории: ")

os.mkdir(dir_name)

print(f"Директория {dir_name} успешно создана")