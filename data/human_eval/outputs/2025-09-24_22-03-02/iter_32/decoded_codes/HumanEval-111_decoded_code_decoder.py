from collections import Counter
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    dict1 = {}
    list1 = test.split(" ")
    t = 0

    counter = Counter(list1)
    for i in list1:
        count_i = counter[i]
        if count_i > t and i != "":
            t = count_i

    if t > 0:
        for i in list1:
            count_i = counter[i]
            if count_i == t:
                dict1[i] = t

    return dict1