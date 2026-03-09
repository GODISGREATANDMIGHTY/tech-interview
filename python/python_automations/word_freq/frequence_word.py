
import re
from collections import Counter

def main():
    FILE_NAME = './log'

    words_freq = Counter()

    words = None
    with open(FILE_NAME, 'r') as f:
        words = f.read()

    words = re.sub(r'[&:,.]', '', words)
    all_words = words.split()
    
    for word in all_words:
        words_freq[word] += 1

    words_freq = dict(sorted(words_freq.items(), key = lambda item : item[1], reverse = True))
    print(words_freq)

    

if __name__ == '__main__':
    main()