from typing import List


def digitSum(data_string: str) -> int:
    if data_string == "":
        return 0

    def recurSum(list_chars: List[str], acc_total: int) -> int:
        if list_chars:
            first_char = list_chars[0]
            if first_char.isupper():
                return recurSum(list_chars[1:], acc_total + ord(first_char))
            else:
                return recurSum(list_chars[1:], acc_total)
        else:
            return acc_total

    return recurSum(list(data_string), 0)