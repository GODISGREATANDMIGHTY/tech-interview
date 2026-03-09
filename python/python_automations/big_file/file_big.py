
import os

def main():
    FILE_DIR = '.'

    big_file_size = 0
    big_file = None
    for file in os.listdir(FILE_DIR):
        if os.path.getsize(os.path.join('.', file)) > big_file_size:
            big_file = os.path.join('.', file)
            big_file_size = os.path.getsize(os.path.join('.', file))

    print(big_file, big_file_size)

if __name__ == '__main__':
    main()