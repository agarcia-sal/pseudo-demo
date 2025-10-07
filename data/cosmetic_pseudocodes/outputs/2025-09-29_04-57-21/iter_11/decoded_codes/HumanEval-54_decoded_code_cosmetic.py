from typing import Set


def same_chars(text_alpha: str, text_beta: str) -> bool:
    chars_alpha: Set[str] = set()
    index_alpha = 0
    while index_alpha < len(text_alpha):
        chars_alpha.add(text_alpha[index_alpha])
        index_alpha += 1

    chars_beta: Set[str] = set()
    index_beta = 0
    while True:
        if index_beta >= len(text_beta):
            break
        chars_beta.add(text_beta[index_beta])
        index_beta += 1

    return chars_alpha == chars_beta