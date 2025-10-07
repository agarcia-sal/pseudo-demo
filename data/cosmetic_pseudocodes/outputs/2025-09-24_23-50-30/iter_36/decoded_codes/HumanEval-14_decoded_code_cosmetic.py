from typing import List

def all_prefixes(input_string: str) -> List[str]:
    accumulation: List[str] = []

    def accumulate_prefix(position: int) -> None:
        if position == len(input_string):
            return
        accumulation.append(input_string[:position + 1])
        accumulate_prefix(position + 1)

    accumulate_prefix(0)
    return accumulation