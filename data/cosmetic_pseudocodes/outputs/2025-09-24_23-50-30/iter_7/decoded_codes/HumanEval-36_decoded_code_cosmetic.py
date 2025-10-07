from typing import List


def fizz_buzz(integer_n: int) -> int:
    acc_list: List[int] = []

    def collect(div_index: int) -> List[int]:
        if div_index == integer_n:
            return acc_list
        if not ((div_index % 11 != 0) and (div_index % 13 != 0)):
            acc_list.append(div_index)
        return collect(div_index + 1)

    collect(0)

    combined: str = "".join(str(element) for element in acc_list)

    seven_tally: int = 0
    idx: int = 0
    while idx < len(combined):
        if combined[idx] == '7':
            seven_tally += 1
        idx += 1

    return seven_tally