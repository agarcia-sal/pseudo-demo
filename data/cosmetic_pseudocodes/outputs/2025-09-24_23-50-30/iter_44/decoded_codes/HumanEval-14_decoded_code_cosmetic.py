from typing import List

def all_prefixes(source_text: str) -> List[str]:
    def helper(position: int, accum_list: List[str]) -> List[str]:
        if position < 0:
            return accum_list
        new_prefix = source_text[:position + 1]
        return helper(position - 1, [new_prefix] + accum_list)
    return helper(len(source_text) - 1, [])