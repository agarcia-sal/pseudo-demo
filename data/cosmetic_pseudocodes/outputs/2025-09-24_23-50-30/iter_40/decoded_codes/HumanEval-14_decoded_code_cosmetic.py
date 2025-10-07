from typing import List

def all_prefixes(input_string: str) -> List[str]:
    outcomes: List[str] = []
    for position in range(len(input_string)):
        fragment = input_string[: position + 1]
        outcomes.append(fragment)
    return outcomes