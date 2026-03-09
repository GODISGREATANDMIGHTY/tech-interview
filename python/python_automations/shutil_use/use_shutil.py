
import os
import shutil

def main():
    FILE_DIR = './f1'

    NEW_FILE_DIR = './f2'
    os.makedirs(NEW_FILE_DIR, exist_ok = True)
    for file in os.listdir(FILE_DIR):
        shutil.copy(os.path.join(FILE_DIR, file), os.path.join(NEW_FILE_DIR, file))

    NEW_FILE_DIR = './f3'
    # os.makedirs(NEW_FILE_DIR, exist_ok = False)
    shutil.copytree(FILE_DIR, NEW_FILE_DIR)

if __name__ == '__main__':
    main()