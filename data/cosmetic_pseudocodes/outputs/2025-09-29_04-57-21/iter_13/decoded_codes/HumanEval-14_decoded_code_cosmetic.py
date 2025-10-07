from typing import List

def all_prefixes(input_string: str) -> List[str]:
    accumulated_prefixes: List[str] = []

    def helper(current_position: int) -> None:
        if current_position == len(input_string):
            return
        prefix_segment = input_string[:current_position + 1]
        accumulated_prefixes.append(prefix_segment)
        helper(current_position + 1)

    helper(0)
    return accumulated_prefixes