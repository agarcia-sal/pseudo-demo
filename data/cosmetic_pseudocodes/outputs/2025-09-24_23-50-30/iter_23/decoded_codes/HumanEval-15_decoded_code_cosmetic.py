from functools import reduce
from typing import List

def string_sequence(integer_alpha: int) -> str:
    string_list: List[str] = []
    index_var: int = 0
    while index_var <= integer_alpha:
        string_list.append(str(index_var))
        index_var += 1
    result_string: str = reduce(lambda acc, elem: acc + " " + elem, string_list, "")
    return result_string[1:]  # remove leading space