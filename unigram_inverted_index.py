import pickle

invertedIndex = {}

def indexFile(i):
    with open(f"processed_files/file{i}.txt", "r") as f:
        words = f.read().split(",")
        for word in words:
            if word not in invertedIndex:
                invertedIndex[word] = set()
            invertedIndex[word].add(i)

def indexAllFiles():
    with open("inverted_index", "wb") as f:
        for i in range(1, 1000):
            indexFile(i)
        pickle.dump(invertedIndex, f)


if __name__ == '__main__':
    indexAllFiles()