
import os
import time

def main():
    FILE_DIR = '.'

    old_files = set(os.listdir(FILE_DIR))
    while True:
        time.sleep(4)

        new_files = set(os.listdir(FILE_DIR))

        diff = new_files - old_files
        if diff:
            print("new files are :", diff)
            old_files = new_files

if __name__ == '__main__':
    main()