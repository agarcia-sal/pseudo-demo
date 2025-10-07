from typing import List


def all_prefixes(input_string: str) -> List[str]:
    accumulator: List[str] = []

    def helper(current_position: int, collected: List[str]) -> List[str]:
        if current_position >= len(input_string):
            return collected
        else:
            return helper(current_position + 1, collected + [input_string[: current_position + 1]])

    return helper(0, accumulator)