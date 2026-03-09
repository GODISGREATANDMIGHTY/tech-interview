import os

def main():
    FILE_DIR = '.'
    MERGED_FILE = './merged.txt'

    with open(MERGED_FILE, 'a') as out_file:
        for file in os.listdir(FILE_DIR):
            if not file.endswith('.txt'):
                continue

            if file == 'merged.txt':
                continue

            with open(file, 'r') as in_file:
                out_file.write(in_file.read() + "\n")

        

if __name__ == '__main__':
    main()