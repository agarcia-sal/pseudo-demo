from typing import List

def is_sorted(lst: List[int]) -> bool:
    count_digit = {i: 0 for i in lst}
    for i in lst:
        count_digit[i] = count_digit[i] + 1
    for i in lst:
        if count_digit[i] > 2:
            return False
    is_ascending = True
    index = 1
    while index < len(lst) and is_ascending == True:
        if lst[index - 1] > lst[index]:
            is_ascending = False
        index += 1
    if is_ascending == True:
        return True
    else:
        return False