from typing import List


def all_prefixes(input_string: str) -> List[str]:
    def collect_prefixes(accumulator: List[str], current_pos: int) -> List[str]:
        if current_pos < 0:
            return accumulator
        return collect_prefixes([input_string[: current_pos + 1]] + accumulator, current_pos - 1)

    return collect_prefixes([], len(input_string) - 1)