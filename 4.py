import os

directory = input("Введите путь к директории: ")

files = os.listdir(directory)

for file in files:
    file_path = os.path.join(directory, file)
    file_size = os.path.getsize(file_path)
    file_creation_time = os.path.getctime(file_path)
    file_info = f"Имя файла: {file}, Размер: {file_size} байт, Дата создания: {file_creation_time}"
    print(file_info)
