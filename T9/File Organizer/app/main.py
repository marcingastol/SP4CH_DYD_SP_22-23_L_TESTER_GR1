import os
from pathlib import Path
from app.file_organizer_logic import organize_files

def main():
    source_directory = Path(os.path.join(os.path.dirname(__file__), '..', 'test_files'))
    destination_directory = os.path.join(os.path.dirname(__file__), '..', 'organized_files')

    file_extensions = {
        'txt': 'Text',
        'jpg': 'Images',
        'pdf': 'Documents'
    }

    organize_files(source_directory, file_extensions, destination_directory)
    print("Files organized successfully!")

if __name__ == '__main__':
    main()
