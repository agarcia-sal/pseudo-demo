from typing import List

def odd_count(lst: List[List[str]]) -> List[str]:
    res = []
    for i in range(len(lst)):
        arr = lst[i]
        n = 0
        for j in range(len(arr)):
            d = arr[j]
            digit_value = int(d)
            if digit_value % 2 == 1:
                n += 1
        constructed_string = (
            "the number of odd elements "
            + str(n)
            + "n the str"
            + str(n)
            + "ng "
            + str(n)
            + " of the "
            + str(n)
            + "nput."
        )
        res.append(constructed_string)
    return res