import os

path = 'C:\Temp'

files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)
    file_info = os.stat(file_path)
    print(f'File name: {file}')
    print(f'Size: {file_info.st_size} bytes')
    print(f'Creation time: {file_info.st_ctime}')
    print()
