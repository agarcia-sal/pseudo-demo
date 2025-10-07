from collections import Counter

def histogram(test):
    word_list = test.split(" ")
    if not word_list:
        return {}

    word_counts = Counter(word_list)
    # Remove empty string counts if present
    if '' in word_counts:
        del word_counts['']

    if not word_counts:
        return {}

    max_count = max(word_counts.values())
    if max_count == 0:
        return {}

    return {word: count for word, count in word_counts.items() if count == max_count}