from typing import List

def odd_count(lst: List[List[str]]) -> List[str]:
    res = []
    for idx in range(len(lst)):
        arr = lst[idx]
        n = 0
        for j in range(len(arr)):
            d = arr[j]
            digit = int(d)
            remainder = digit % 2
            if remainder == 1:
                n += 1
        str_n = str(n)
        constructed_string = "the number of odd elements " + str_n + "n the str" + str_n + "ng " + str_n + " of the " + str_n + "nput."
        res.append(constructed_string)
    return res