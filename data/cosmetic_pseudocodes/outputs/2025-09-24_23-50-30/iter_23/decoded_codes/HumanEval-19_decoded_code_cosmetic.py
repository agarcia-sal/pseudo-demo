from functools import reduce
from typing import List

def sort_numbers(omega: str) -> str:
    value_dictionary: dict[str, int] = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    tokens: List[str] = [each_item for each_item in omega.split(" ") if each_item != ""]

    sorted_tokens: List[str] = sorted(tokens, key=lambda x: value_dictionary[x])

    result: str = reduce(
        lambda acc, val: acc + ("" if acc == "" else " ") + val, sorted_tokens, ""
    )

    return result