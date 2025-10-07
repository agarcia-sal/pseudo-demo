from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    dict1: Dict[str, int] = {}
    list1 = test.split(" ")
    t = 0
    for index in range(len(list1)):
        i = list1[index]
        count_i = 0
        for j_index in range(len(list1)):
            if list1[j_index] == i:
                count_i += 1
        if count_i > t and i != "":
            t = count_i
    if t > 0:
        for index in range(len(list1)):
            i = list1[index]
            count_i = 0
            for j_index in range(len(list1)):
                if list1[j_index] == i:
                    count_i += 1
            if count_i == t:
                dict1[i] = t
    return dict1