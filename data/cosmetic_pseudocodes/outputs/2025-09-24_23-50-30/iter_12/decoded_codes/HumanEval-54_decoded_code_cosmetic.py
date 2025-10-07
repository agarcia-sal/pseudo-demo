from typing import Set


def same_chars(text_alpha: str, text_beta: str) -> bool:
    character_set_alpha: Set[str] = set(text_alpha)
    character_set_beta: Set[str] = set(text_beta)
    return character_set_alpha == character_set_beta