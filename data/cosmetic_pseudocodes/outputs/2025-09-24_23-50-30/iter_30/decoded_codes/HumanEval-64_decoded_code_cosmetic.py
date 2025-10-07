from typing import Set


def vowels_count(str_param: str) -> int:
    vow_set: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    def count_items(s: str, acc: int, idx: int) -> int:
        if idx == len(s):
            return acc
        if s[idx] in vow_set:
            return count_items(s, acc + 1, idx + 1)
        return count_items(s, acc, idx + 1)

    tally: int = count_items(str_param, 0, 0)

    if str_param and (str_param[-1] == "y" or str_param[-1] == "Y"):
        tally += 1

    return tally