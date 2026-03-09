from collections import Counter

def main():
    LOG_FILE_NAME = './log'
    contents = []
    with open(LOG_FILE_NAME, 'r') as f:
        contents = f.read().splitlines()

    counter = Counter()
    for content in contents:
        if not content:
            continue

        if 'ERROR' in content:
            counter[content] += 1

    return counter.most_common(3)


if __name__ == '__main__':
    vals = main()

    for v in vals:
        log, counter = v
        print(log, counter)