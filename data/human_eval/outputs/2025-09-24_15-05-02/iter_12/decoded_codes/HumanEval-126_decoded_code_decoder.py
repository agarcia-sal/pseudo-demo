from typing import List

def is_sorted(lst: List[int]) -> bool:
    count_digit = {num: 0 for num in lst}
    for number in lst:
        count_digit[number] += 1
    if any(count_digit[number] > 2 for number in lst):
        return False
    if all(lst[i - 1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False