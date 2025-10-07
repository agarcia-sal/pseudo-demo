from typing import Set

def same_chars(Alpha: str, Bravo: str) -> bool:
    def build_set(BRAVO: str, INDEX: int, ACCUMULATOR: Set[str]) -> Set[str]:
        if INDEX < len(BRAVO):
            HEAD = BRAVO[INDEX]
            UPDATED_SET = ACCUMULATOR | {HEAD}
            return build_set(BRAVO, INDEX + 1, UPDATED_SET)
        else:
            return ACCUMULATOR

    set_alpha = build_set(Alpha, 0, set())
    set_bravo = build_set(Bravo, 0, set())

    return set_alpha == set_bravo