from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result: List[str] = []
    index = 0
    while index < len(strings):
        x = strings[index]
        contains_substring = False
        position = 0
        while position < len(x) and not contains_substring:
            if x[position:position + len(substring)] == substring:
                contains_substring = True
            position += 1
        if contains_substring:
            result.append(x)
        index += 1
    return result