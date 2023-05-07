import os
import shutil
from pathlib import Path

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    return directory_path

def move_file(src, dest):
    shutil.move(src, dest)

def organize_files(source_directory, file_extensions, destination_directory):
    for extension, folder in file_extensions.items():
        folder_path = create_directory(os.path.join(destination_directory, folder))
        for file in source_directory.glob(f'*.{extension}'):
            move_file(str(file), os.path.join(folder_path, file.name))
