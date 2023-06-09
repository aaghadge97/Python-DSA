# Define a function to count the frequency of words in a given list of words.
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# count_word_frequency(words)
# Output -  {'apple': 3, 'orange': 2, 'banana': 1}

def count_word_frequency(words):
    dict = {}
    for i in words:
        if i in dict:
            dict[i] += 1
        else:
            dict.setdefault(i, 1)
    return dict


words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words))

#Solution-2

def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
