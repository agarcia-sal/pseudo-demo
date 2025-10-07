from typing import List

def all_prefixes(input_string: str) -> List[str]:
    result = []
    for index in range(len(input_string)):
        prefix = input_string[:index + 1]
        result.append(prefix)
    return result