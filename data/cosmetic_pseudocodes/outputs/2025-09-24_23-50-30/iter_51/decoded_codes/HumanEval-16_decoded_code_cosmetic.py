from typing import Set

def count_distinct_characters(string_input: str) -> int:
    def helper_index(seq: str, idx: int, acc_set: Set[str]) -> int:
        if idx == len(seq):
            return len(acc_set)
        ch = seq[idx].lower()
        new_set = acc_set | {ch}
        return helper_index(seq, idx + 1, new_set)
    return helper_index(string_input, 0, set())