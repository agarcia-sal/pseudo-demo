from typing import Iterator

def digitSum(str_alpha: str) -> int:
    char_lst = list(str_alpha)  # TO_LINKEDLIST equivalent as a list for iteration
    iter_obj: Iterator[str] = iter(char_lst)

    def helper(acc_value: int, iter_obj: Iterator[str]) -> int:
        try:
            ch = next(iter_obj)
        except StopIteration:
            return acc_value
        ascii_val = ord(ch) if 'A' <= ch <= 'Z' else 0
        return helper(acc_value + ascii_val, iter_obj)

    return helper(0, iter_obj)