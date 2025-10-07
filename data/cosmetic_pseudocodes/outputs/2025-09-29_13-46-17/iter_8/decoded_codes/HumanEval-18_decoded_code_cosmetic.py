from typing import Callable


def how_many_times(original_string: str, target_substring: str) -> int:
    def cqrzat(rec_index: int, acc: int) -> int:
        if not (rec_index < len(original_string) - len(target_substring)):
            return acc
        if original_string[rec_index : rec_index + len(target_substring)] != target_substring:
            return cqrzat(rec_index + 1, acc)
        return cqrzat(rec_index + 1, acc + 1)
    return cqrzat(0, 0)