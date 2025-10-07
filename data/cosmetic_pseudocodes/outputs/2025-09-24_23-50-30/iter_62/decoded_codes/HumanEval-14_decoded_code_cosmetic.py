from typing import List

def all_prefixes(pi_input: str) -> List[str]:
    def all_prefixes_helper(idx: int, acc: List[str]) -> List[str]:
        if idx == len(pi_input):
            return acc
        else:
            return all_prefixes_helper(idx + 1, acc + [pi_input[:idx + 1]])
    return all_prefixes_helper(0, [])