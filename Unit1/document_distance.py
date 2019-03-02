import string
import numpy as np
import math

def document_distance(file1, file2):
    d1, d2 = count_frequencies(file1, file2)
    similarity = inner_product_sim(d1, d2)
    return similarity

def count_frequencies(file1, file2):
    words1 = get_words_from_file(file1)
    words2 = get_words_from_file(file2)
    d1 = get_frequency_dictionary(words1)
    d2 = get_frequency_dictionary(words2)
    return d1, d2
    
def get_words_from_file(f):
    contents = open(f, 'r').read()
    trans_table = str.maketrans(string.punctuation,
                                   " " * len(string.punctuation))
    words = str.translate(contents, trans_table)
    words = contents.lower()
    words = contents.split()
    return words

def get_frequency_dictionary(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def inner_product_sim(d1, d2):
    numer = inner_product(d1, d2)
    denom = math.sqrt(inner_product(d1, d1) * inner_product(d2, d2))
    return numer / denom

def inner_product(d1, d2):
    result = 0.0
    for word, freq1 in d1.items():
        if word in d2:
            freq2 = d2[word]
            result += freq1 * freq2 
    return result

if __name__ == "__main__":
    f1 = "document_distance.py"
    f2 = "document_distance.py"
    sim = document_distance(f1, f2)
    print(sim)
    
    
