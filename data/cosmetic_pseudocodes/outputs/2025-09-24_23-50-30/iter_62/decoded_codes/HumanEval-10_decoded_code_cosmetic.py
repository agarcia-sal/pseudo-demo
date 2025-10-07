from typing import Callable

def is_palindrome(str_param: str) -> bool:
    return str_param == str_param[::-1]

def make_palindrome(str_param: str) -> str:
    if len(str_param) == 0:
        return ""

    def search_index(index_param: int) -> int:
        if is_palindrome(str_param[index_param:]):
            return index_param
        else:
            return search_index(index_param + 1)

    pos_var: int = search_index(0)
    return str_param + str_param[:pos_var][::-1]