from typing import Set

def same_chars(p1: str, p2: str) -> bool:
    def to_character_set(q: str) -> Set[str]:
        def loop(w: str, acc: Set[str]) -> Set[str]:
            if not w:
                return acc
            return loop(w[1:], acc | {w[0]})
        return loop(q, set())
    return to_character_set(p1) == to_character_set(p2)