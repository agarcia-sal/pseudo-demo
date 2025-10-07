from typing import List

def all_prefixes(input_string: str) -> List[str]:
    accumulator: List[str] = []
    iterator: int = 0

    while iterator < len(input_string):
        current_prefix: str = input_string[:iterator + 1]
        accumulator.append(current_prefix)
        iterator += 1

    return accumulator