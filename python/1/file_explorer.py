
import sys
import shutil
from pathlib import Path

if __name__ == '__main__':
    input_dir = '../1'

    directory = Path(input_dir)
    if not directory.is_dir():
        print(f'{input_dir} is not a directory')
        sys.exit(1)

    for file in directory.iterdir():
        if not file.is_file():
            continue

        if not file.name.endswith(".txt"):
            continue

        new_file_name = file.name.lower()
        print(new_file_name)
        shutil.move(file, new_file_name)
        

        
