from typing import Iterable

def same_chars(character_sequence_alpha: Iterable[str], character_sequence_beta: Iterable[str]) -> bool:
    set_alpha = set()
    set_beta = set()

    for element in character_sequence_alpha:
        set_alpha.add(element)

    for element in character_sequence_beta:
        set_beta.add(element)

    return set_alpha == set_beta