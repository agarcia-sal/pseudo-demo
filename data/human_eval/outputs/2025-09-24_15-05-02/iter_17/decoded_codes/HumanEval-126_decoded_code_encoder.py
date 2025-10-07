from typing import List, Dict

def is_sorted(lst: List[int]) -> bool:
    count_digit: Dict[int, int] = {element: 0 for element in lst}
    for i in lst:
        count_digit[i] += 1
    if any(count > 2 for count in count_digit.values()):
        return False
    if all(lst[i - 1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False