from typing import List


def sorted_list_sum(list_of_strings: List[str]) -> List[str]:
    list_of_strings.sort()
    new_list: List[str] = [s for s in list_of_strings if len(s) % 2 == 0]
    return sorted(new_list, key=len)