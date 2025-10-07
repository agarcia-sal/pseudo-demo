from typing import List


def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output: List[int] = []
    pick_min: int = 1
    for _ in range(len(list_of_integers)):
        if pick_min == 1:
            val = list_of_integers[0]
            for num in list_of_integers:
                if num < val:
                    val = num
        else:
            val = list_of_integers[0]
            for num in list_of_integers:
                if num > val:
                    val = num
        output.append(val)
        list_of_integers.remove(val)
        pick_min *= -1
    return output