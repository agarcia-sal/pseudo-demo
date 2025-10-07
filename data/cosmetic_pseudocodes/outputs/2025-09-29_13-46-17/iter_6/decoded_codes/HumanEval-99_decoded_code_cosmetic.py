from math import floor, ceil
from typing import Callable


def closest_integer(value: str) -> int:
    def truncate_trailing_zeros(strVal: str, acc: str) -> str:
        if not strVal or strVal[-1] != '0':
            return acc + strVal
        else:
            return truncate_trailing_zeros(strVal[:-1], acc)

    def ends_with(strX: str, suffix: str) -> bool:
        return len(suffix) <= len(strX) and strX[-len(suffix):] == suffix

    def count_occurrences(haystack: str, needle: str, idx: int, cnt: int) -> int:
        if idx >= len(haystack):
            return cnt
        else:
            return count_occurrences(haystack, needle, idx + 1, cnt + (1 if haystack[idx] == needle else 0))

    def to_integer_round(num: float) -> int:
        return floor(num + 0.5)

    def select_result(numVal: float, strVal: str) -> int:
        if ends_with(strVal, '.5'):
            return ceil(numVal) if numVal > 0 else floor(numVal)
        elif len(strVal) > 0:
            return to_integer_round(numVal)
        else:
            return 0

    total_dots = count_occurrences(value, '.', 0, 0)
    trimmed_value = truncate_trailing_zeros(value, '') if total_dots == 1 else value
    numeric_value = float(trimmed_value)
    return select_result(numeric_value, trimmed_value)