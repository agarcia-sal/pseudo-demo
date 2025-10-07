from typing import List

def all_prefixes(input_string: str) -> List[str]:
    def inner(index: int, acc: List[str]) -> List[str]:
        if index < len(input_string):
            return inner(index + 1, acc + [input_string[:index + 1]])
        else:
            return acc
    return inner(0, [])