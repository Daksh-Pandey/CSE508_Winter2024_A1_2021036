import pickle

positionalIndex = {}

def indexFile(i):
    with open(f"processed_files/file{i}.txt") as f:
        text = f.read().split(",")
    for j in range(len(text)):
        word = text[j]
        if word in positionalIndex:
            if i in positionalIndex[word]:
                positionalIndex[word][i].add(j+1)
            else:
                positionalIndex[word][i] = {j+1}
        else:
            positionalIndex[word] = {i : {j+1}}

def indexAllFiles():
    with open("positional_index", "wb") as f:
        for i in range(1, 1000):
            indexFile(i)
        pickle.dump(positionalIndex, f)


if __name__ == '__main__':
    indexAllFiles()