from typing import List

def all_prefixes(input_string: str) -> List[str]:
    accumulator: List[str] = []
    counter: int = 0
    while counter < len(input_string):
        accumulator.append(input_string[:counter + 1])
        counter += 1
    return accumulator