from typing import Set


def same_chars(para_alpha: str, para_beta: str) -> bool:
    def collect_chars(str_input: str) -> Set[str]:
        index_pos: int = 0
        char_set: Set[str] = set()
        while index_pos < len(str_input):
            char_set.add(str_input[index_pos])
            index_pos += 1
        return char_set

    return collect_chars(para_alpha) == collect_chars(para_beta)