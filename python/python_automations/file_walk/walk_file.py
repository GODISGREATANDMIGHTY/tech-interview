
import os

def main():
    FILE_DIR = '..'

    for root, dirs, files in os.walk(FILE_DIR):
        for file in files:
            if not file.endswith('.py'):
                continue

            print("full path is ", os.path.join(root, file))

if __name__ == '__main__':
    main()