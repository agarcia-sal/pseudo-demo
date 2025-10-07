from typing import List

def all_prefixes(original_input: str) -> List[str]:
    def helper(counter: int, accumulator: List[str]) -> List[str]:
        if counter > len(original_input) - 1:
            return accumulator
        return helper(counter + 1, accumulator + [original_input[:counter + 1]])
    return helper(0, [])