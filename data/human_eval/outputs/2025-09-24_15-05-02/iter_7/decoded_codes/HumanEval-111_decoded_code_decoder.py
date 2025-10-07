from collections import Counter

def histogram(test):
    dict1 = {}
    list1 = test.split(" ")
    counts = Counter(filter(None, list1))  # filter out empty strings
    if not counts:
        return dict1
    t = max(counts.values())
    for word, count in counts.items():
        if count == t:
            dict1[word] = t
    return dict1