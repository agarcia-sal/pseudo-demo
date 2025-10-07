from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    dict1: Dict[str, int] = {}
    list1 = test.split(" ")
    t = 0
    length = len(list1)
    for index1 in range(length):
        i = list1[index1]
        count_i = 0
        for index2 in range(length):
            if list1[index2] == i:
                count_i += 1
        if count_i > t and i != "":
            t = count_i
    if t > 0:
        for index3 in range(length):
            i = list1[index3]
            count_i = 0
            for index4 in range(length):
                if list1[index4] == i:
                    count_i += 1
            if count_i == t and i not in dict1 and i != "":
                dict1[i] = t
    return dict1