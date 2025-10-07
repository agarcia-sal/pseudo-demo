from typing import List, Dict

def is_sorted(list_of_numbers: List[int]) -> bool:
    count_map: Dict[int, int] = {}
    flag: int = 0

    def inner_count(params: List[int]) -> int:
        nonlocal flag
        if len(params) == 0:
            return flag
        head = params[0]
        if head in count_map:
            count_map[head] += 1
            if count_map[head] > 2:
                flag = 1
        else:
            count_map[head] = 1
        return inner_count(params[1:])

    inner_count(list_of_numbers)
    if flag == 1:
        return False

    def check_sorted(index: int) -> bool:
        if index >= len(list_of_numbers):
            return True
        prev = list_of_numbers[index - 1]
        curr = list_of_numbers[index]
        if not (curr < prev):
            return check_sorted(index + 1)
        else:
            return False

    return check_sorted(1)