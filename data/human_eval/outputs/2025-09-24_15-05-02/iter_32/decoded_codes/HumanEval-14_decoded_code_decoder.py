from typing import List

def all_prefixes(input_string: str) -> List[str]:
    return [input_string[:index + 1] for index in range(len(input_string))]