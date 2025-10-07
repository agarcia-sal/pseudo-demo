from typing import List

def all_prefixes(input_string: str) -> List[str]:
    def helper(current_pos: int, accum: List[str]) -> List[str]:
        if current_pos >= len(input_string):
            return accum

        new_prefix = "".join(input_string[idx] for idx in range(current_pos + 1))
        accum.append(new_prefix)
        return helper(current_pos + 1, accum)

    return helper(0, [])