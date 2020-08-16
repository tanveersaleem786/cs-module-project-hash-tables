import random

start_words = {}
word_store = {}


def store_words(storage_type, word, next_word):
    if word not in storage_type:
        storage_type[word] = [next_word]
    else:
        storage_type[word].append(next_word)


# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    text = f.read()
    #text = "Cats and dogs and birds and fish dogs birds"
    # TODO: analyze which words can follow other words
    words_list = text.split()
    for (index, cur_word) in enumerate(words_list):
        # for getting next word
        next_word = words_list[index+1] if index < len(words_list)-1 else ""

        # checking  for start word
        if cur_word[0].isupper() or (cur_word[0] == "\"" and cur_word[1].isupper()):
            store_words(start_words, cur_word, next_word)
        else:
            store_words(word_store, cur_word, next_word)

    # TODO: construct 5 random sentences
    print(start_words)
    print(word_store)