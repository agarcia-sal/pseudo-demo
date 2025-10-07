from typing import List

def all_prefixes(input_string: str) -> List[str]:
    return [input_string[:pos + 1] for pos in range(len(input_string))]