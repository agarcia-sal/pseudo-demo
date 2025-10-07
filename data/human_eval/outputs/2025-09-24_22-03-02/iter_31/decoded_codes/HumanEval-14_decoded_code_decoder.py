from typing import List

def all_prefixes(string: str) -> List[str]:
    result = ['']
    length_of_string = len(string)
    i = 0
    while i < length_of_string:
        prefix = ''
        j = 0
        while j <= i:
            prefix += string[j]
            j += 1
        result.append(prefix)
        i += 1
    return result