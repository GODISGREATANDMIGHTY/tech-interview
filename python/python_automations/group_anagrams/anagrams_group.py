

def main(words):
    d = dict()

    for word in words:
        k = ''.join(sorted(word))
        if not k in d:
            l = []
            l.append(word)
            d[k] = l
        else:
            d[k].append(word)

    for _, v in d.items():
        print(v)

if __name__ == '__main__':
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]

    main(words)