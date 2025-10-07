from collections import Counter

def histogram(test):
    words = test.split(" ")
    word_counts = Counter(words)
    max_count = 0

    for word in words:
        if word and word_counts[word] > max_count:
            max_count = word_counts[word]

    result = {}
    if max_count > 0:
        for word in words:
            if word_counts[word] == max_count:
                result[word] = max_count

    return result