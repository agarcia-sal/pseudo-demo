from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result: List[int] = []
    flag: bool = True

    def loop(lst: List[int]) -> List[int]:
        nonlocal flag, result
        if not lst:
            return result
        s = min(lst) if flag else max(lst)
        result.append(s)
        lst = [x for x in lst if x != s]
        flag = not flag
        return loop(lst)

    return loop(list_of_integers)