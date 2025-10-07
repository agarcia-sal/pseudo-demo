from typing import List

def all_prefixes(input_string: str) -> List[str]:
    return [input_string[:i + 1] for i in range(len(input_string))]