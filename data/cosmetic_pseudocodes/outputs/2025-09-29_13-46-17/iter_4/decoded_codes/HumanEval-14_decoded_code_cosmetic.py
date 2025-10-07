from typing import List


def all_prefixes(input_string: str) -> List[str]:
    def gather_prefixes(idx: int, acc: List[str]) -> List[str]:
        if idx < 0:
            return acc
        else:
            current_prefix = input_string[: idx + 1]
            return gather_prefixes(idx - 1, [current_prefix] + acc)

    return gather_prefixes(len(input_string) - 1, [])