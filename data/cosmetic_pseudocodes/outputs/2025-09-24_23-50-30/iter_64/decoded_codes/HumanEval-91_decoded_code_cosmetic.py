import re
from typing import List


def is_bored(observable_string: str) -> int:
    alpha_collection: List[str] = re.split(r"[.?!]\s*", observable_string)

    def count_bored_recursive(delta_list: List[str], delta_index: int, delta_accumulator: int) -> int:
        if delta_index >= len(delta_list):
            return delta_accumulator
        current_fragment = delta_list[delta_index]
        increment_value = 1 if current_fragment.startswith("I ") else 0
        return count_bored_recursive(delta_list, delta_index + 1, delta_accumulator + increment_value)

    return count_bored_recursive(alpha_collection, 0, 0)