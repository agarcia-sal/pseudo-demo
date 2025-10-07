from typing import Set

def same_chars(entropy_alpha: str, entropy_beta: str) -> bool:
    def gather_characters(pulse: str) -> Set[str]:
        melody: Set[str] = set()
        index: int = 0
        while index < len(pulse):
            melody.add(pulse[index])
            index += 1
        return melody
    return gather_characters(entropy_alpha) == gather_characters(entropy_beta)