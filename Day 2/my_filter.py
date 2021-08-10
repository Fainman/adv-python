#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/10/2021
Purpose: Review the filter() function, functools
"""

from functools import reduce
import operator


def count_words(doc):
    """Count words in a document
    Produces a dictionary mappying words"""
    # normalize the string
    normalize_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalize_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

def combine_counts(d1, d2):
    """Combine two word dictionaries"""
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d

# --------------------------------------------------
def main():
    """Explore filter functions"""
    numbers = [2, 5, 8, -1, 90, -2, -33, 12]
    # Task: Create a list of all positive numbers
    positives = [x for x in numbers if x >= 0]
    print(positives)

    # filter()
    positives = list(filter(lambda x: x > 0, numbers))
    print(positives)

    negatives = list(filter(None, numbers))
    print(negatives)

    # Simple code (reduce next)
    accumulator = operator.add(numbers[0], numbers[1])
    for item in numbers[2:]:
        accumulator = operator.add(accumulator, item)
    print(accumulator)

    # Use reduce
    print(reduce(operator.add, numbers))

    # Combine map() and reduce()
    document = 'It was the best of times, it was the worst of times'
    print(count_words(document))
    documents = [
        'It was the best of times, it was the worst of times.',
        'I went to the woods because I wished to live deliberately, to front only the essential facts of life...',
        'Friends, Romans, countrymen, lend me your ears; I come to bury Caesar, not to praise him.',
        'I do not like green eggs and ham. I do not like them, Sam-I-Am.'
    ]

    counts = map(count_words, documents)
    total_counts = reduce(combine_counts, counts)

    print(total_counts)

# --------------------------------------------------
if __name__ == '__main__':
    main()
