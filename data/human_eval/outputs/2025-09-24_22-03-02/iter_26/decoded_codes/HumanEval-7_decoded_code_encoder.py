from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result = []
    for x in strings:
        contains_substring = False
        for substring_index in range(len(x) - len(substring) + 1):
            match = True
            for char_index in range(len(substring)):
                if x[substring_index + char_index] != substring[char_index]:
                    match = False
                    break
            if match:
                contains_substring = True
                break
        if contains_substring:
            result.append(x)
    return result