import time
import preprocessing
import unigram_inverted_index
import boolean_queries
import positional_index
import phrase_queries

loop = True

while(loop):
    print("\n\n")
    time.sleep(1)
    print("==============================================================================")
    print("Welcome to Information Retrieval Assignment 1 by Daksh Pandey...")
    print("-----------------------------------------------------------------")
    print("Choose below options to perform:")
    print("[1] Preprocess text files")
    print("[2] Construct unigram inverted index")
    print("[3] Enter boolean query to the inverted index")
    print("[4] Construct positional index")
    print("[5] Enter phrase query to positional index")
    print("[6] Exit")
    print("==============================================================================")

    option = int(input("Enter option: "))

    if option == 1:
        preprocessing.preProcess()
        print("\nAll text files preprocessed!!")

    elif option == 2:
        unigram_inverted_index.indexAllFiles()
        print("\nCreated inverted index!!")

    elif option == 3:
        n = int(input())
        inputs = []
        operations = []
        for i in range(n):
            text = input()
            ops = input()
            inputs.append(text)
            operations.append(ops)
        boolean_queries.execQueries(n, inputs, operations)

    elif option == 4:
        positional_index.indexAllFiles()
        print("\nCreated positional index!!")

    elif option == 5:
        n = int(input())
        textList = []
        for i in range(n):
            text = input()
            textList.append(text)
        phrase_queries.execQueries(n, textList)

    elif option == 6:
        loop = False
