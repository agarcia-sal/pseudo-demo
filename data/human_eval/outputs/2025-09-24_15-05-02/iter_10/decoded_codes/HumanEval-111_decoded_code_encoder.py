from collections import Counter

def histogram(test):
    word_counts = Counter(test.split(" "))
    max_count = 0

    for word in word_counts:
        if word != "" and word_counts[word] > max_count:
            max_count = word_counts[word]

    result = {}
    if max_count > 0:
        for word, count in word_counts.items():
            if count == max_count:
                result[word] = count

    return result