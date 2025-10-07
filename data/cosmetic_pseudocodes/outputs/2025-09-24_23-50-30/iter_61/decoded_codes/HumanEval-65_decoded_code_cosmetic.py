from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    string_list: List[str] = []
    integer_length: int = 0

    def build_list(pos: int) -> None:
        nonlocal integer_length
        s = str(integer_x)
        if pos == len(s):
            integer_length = pos
        else:
            string_list.append(s[pos])
            build_list(pos + 1)

    build_list(0)

    def reverse_list(input_list: List[str], idx: int, acc: str) -> str:
        if idx < 0:
            return acc
        else:
            return reverse_list(input_list, idx - 1, acc + input_list[idx])

    def circular_rec(i: int, acc1: str, acc2: str) -> str:
        if i < integer_length - integer_shift:
            return circular_rec(i + 1, acc1, acc2 + string_list[i])
        elif i < integer_length:
            return circular_rec(i + 1, acc1 + string_list[i], acc2)
        else:
            return acc1 + acc2

    if integer_shift > integer_length:
        return reverse_list(string_list, integer_length - 1, "")
    else:
        return circular_rec(integer_length - integer_shift, "", "")