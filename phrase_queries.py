import pickle
import preprocessing

def execQuery(text):
    text = preprocessing.preProcessString(text)
    with open("positional_index", "rb") as f:
        db = pickle.load(f)
    if text[0] in db:
        docsWithWords = set(db[text[0]].keys())
    else:
        docsWithWords = set()
    for i in range(1, len(text)):
        if text[i] in db:
            docsWithWords &= set(db[text[i]].keys())
        else:
            docsWithWords = set()
            break
    docsWithWords = list(docsWithWords)
    if len(docsWithWords) == 0:
        return docsWithWords
    result_set = list()
    for doc in docsWithWords:
        positions = db[text[0]][doc]
        for i in range(1, len(text)):
            bw2words = set()
            nextWord = text[i]
            for pos in positions:
                if pos+1 in db[nextWord][doc]:
                    bw2words.add(pos+1)
            positions = bw2words
        if len(positions) != 0:
            result_set.append(doc)
    return sorted(result_set)

def execQueries(n, textList):
    for i in range(n):
        doc_set = execQuery(textList[i])
        if len(doc_set) == 0:
            print(f"No document exists for query {i+1} !!")
            continue
        print(f"Number of documents retrieved for query {i+1}: ", len(doc_set))
        print(f"Names of the documents retrieved for query {i+1}: ")
        for i in doc_set:
            print(f"file{i}.txt", end = '  ')
        print()
    print()