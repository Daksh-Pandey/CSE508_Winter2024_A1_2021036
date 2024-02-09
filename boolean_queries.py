import pickle
import preprocessing

universal_set = set(i for i in range(1, 1000))

def execQuerywithOps(text, operations):
    text = preprocessing.preProcessString(text)
    operations = operations.split(',')
    for i in range(len(operations)):
        operations[i] = operations[i].strip()
    query = ""
    for i in range(len(text) - 1):
        query += text[i] + " "
        query += operations[i] + " "
    query += text[len(text) - 1]
    with open("inverted_index", "rb") as f:
        db = pickle.load(f)
    if text[0] in db:
        result_set = db[text[0]]
    else:
        result_set = set()
    for i in range(len(operations)):
        operation = operations[i]
        word = text[i+1]
        if word in db:
            docsWithWord = db[word]
        else:
            docsWithWord = set()
        if operation == "AND":
            result_set = result_set & docsWithWord
        elif operation == "OR":
            result_set = result_set | docsWithWord
        elif operation == "AND NOT":
            result_set &= universal_set - docsWithWord
        elif operation == "OR NOT":
            result_set |= universal_set - docsWithWord
    result_set = sorted(list(result_set))
    return [query, result_set]

def execQuerywithoutOps(word):
    word = preprocessing.preProcessString(word)
    word = word[0]
    with open("inverted_index", "rb") as f:
        db = pickle.load(f)
    if word in db:
        docsWithWord = db[word]
    else:
        docsWithWord = set()
    return [word, sorted(list(docsWithWord))]

def execQueries(n, wordsList, opsList):
    for i in range(n):
        if opsList[0] == "":
            returnedList = execQuerywithoutOps(wordsList[0])
        else:
            returnedList = execQuerywithOps(wordsList[i], opsList[i])
        query = returnedList[0]
        doc_set = returnedList[1]
        print(f"Query {i+1}: ", query)
        if len(doc_set) == 0:
            print(f"No document exists for query {i+1} !!")
            continue
        print(f"Number of documents retrieved for query {i+1}: ", len(doc_set))
        print(f"Names of the documents retrieved for query {i+1}: ")
        for i in doc_set:
            print(f"file{i}.txt", end = '  ')
        print()
    print()