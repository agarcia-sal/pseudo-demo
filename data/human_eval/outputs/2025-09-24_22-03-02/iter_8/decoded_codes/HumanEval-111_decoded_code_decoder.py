from collections import Counter
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    dict1 = {}
    list1 = test.split(" ")
    t = 0

    counts = Counter(list1)
    for i in list1:
        if counts[i] > t and i != "":
            t = counts[i]

    if t > 0:
        for i in list1:
            if counts[i] == t:
                dict1[i] = t

    return dict1