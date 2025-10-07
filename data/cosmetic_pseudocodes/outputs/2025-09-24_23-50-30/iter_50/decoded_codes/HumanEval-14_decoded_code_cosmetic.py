from typing import List


def all_prefixes(input_string: str) -> List[str]:
    accumulator: List[str] = []
    iterator: int = 0
    while iterator < len(input_string):
        temp_str: str = ""
        sub_iterator: int = 0
        while sub_iterator <= iterator:
            temp_str += input_string[sub_iterator]
            sub_iterator += 1
        accumulator.append(temp_str)
        iterator += 1
    return accumulator