import os
import pytest
from pathlib import Path
from app.file_organizer_logic import create_directory, move_file, organize_files

def test_create_directory():
    test_dir = 'test_directory'
    create_directory(test_dir)
    assert os.path.exists(test_dir)
    os.rmdir(test_dir)

def test_move_file(tmp_path):
    src_file = tmp_path / "test.txt"
    src_file.write_text("Test content")
    dest_file = tmp_path / "moved_test.txt"
    move_file(src_file, dest_file)
    assert not src_file.exists()
    assert dest_file.exists()

def test_organize_files(tmp_path):
    source_directory = tmp_path / "source"
    source_directory.mkdir()
    destination_directory = tmp_path / "destination"

    file_extensions = {
        'txt': 'Text',
        'jpg': 'Images',
        'pdf': 'Documents'
    }

    test_files = ['file1.txt', 'file2.jpg', 'file3.pdf']
    for file_name in test_files:
        (source_directory / file_name).write_text("Test content")

    organize_files(source_directory, file_extensions, destination_directory)

    for file_name, folder in zip(test_files, file_extensions.values()):
        assert not (source_directory / file_name).exists()
        assert (destination_directory / folder / file_name).exists()
