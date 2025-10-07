from typing import Set


def same_chars(alpha: str, beta: str) -> bool:
    def build_set(chars: str, idx: int, accumulator: Set[str]) -> Set[str]:
        if idx == len(chars):
            return accumulator
        temp_set = accumulator | {chars[idx]}
        return build_set(chars, idx + 1, temp_set)

    set_A = build_set(alpha, 0, set())
    set_B = build_set(beta, 0, set())
    difference = (set_A - set_B) | (set_B - set_A)
    return difference == set()