from typing import List

def sort_third(l: List) -> List:
    l = list(l)
    indexes_to_sort = []
    values_to_sort = []
    i = 0
    while i < len(l):
        if i % 3 == 0:
            indexes_to_sort.append(i)
            values_to_sort.append(l[i])
        i += 1
    values_to_sort.sort()
    j = 0
    while j < len(indexes_to_sort):
        l[indexes_to_sort[j]] = values_to_sort[j]
        j += 1
    return l