from typing import List

def odd_count(lst: List[str]) -> List[str]:
    res: List[str] = []
    for index_i in range(len(lst)):
        arr = lst[index_i]
        n = 0
        for index_d in range(len(arr)):
            d_char = arr[index_d]
            d_int = int(d_char)
            d_mod = d_int % 2
            if d_mod == 1:
                n += 1
        s = "the number of odd elements " + str(n) + "n the str" + str(n) + "ng " + str(n) + " of the " + str(n) + "nput."
        res.append(s)
    return res