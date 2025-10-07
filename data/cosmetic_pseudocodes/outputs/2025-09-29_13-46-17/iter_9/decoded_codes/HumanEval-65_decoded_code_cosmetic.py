from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    acc_str: List[str] = []  # accumulator for characters of integer_x string form
    length_store: int = 0
    x = integer_x
    shift = integer_shift

    def rec_str(z: int) -> None:
        if z < 10:
            acc_str.append(str(z))
        else:
            rec_str(z // 10)
            acc_str.append(str(z % 10))

    rec_str(x)
    length_store = len(acc_str)

    if not (shift <= length_store):
        rev_str: List[str] = []

        def rev_proc(i: int) -> None:
            if i <= 0:
                return
            rev_str.append(acc_str[i - 1])
            rev_proc(i - 1)

        rev_proc(length_store)
        return "".join(rev_str)

    k = length_store - shift

    first_part: List[str] = []
    second_part: List[str] = []

    def first_proc(start: int, end: int) -> None:
        if start > end:
            return
        first_part.append(acc_str[start - 1])
        first_proc(start + 1, end)

    def second_proc(start: int, end: int) -> None:
        if start > end:
            return
        second_part.append(acc_str[start - 1])
        second_proc(start + 1, end)

    first_proc(k + 1, length_store)
    second_proc(1, k)

    return "".join(first_part + second_part)