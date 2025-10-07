from typing import List

def filter_by_substring(array_tokens: List[str], token_substring: str) -> List[str]:
    accumulator: List[str] = []
    for element in array_tokens:
        if token_substring in element:
            accumulator.append(element)
    return accumulator