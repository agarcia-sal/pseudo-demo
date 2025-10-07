from typing import Sequence

def vowels_count(alpha_tokens: Sequence[str]) -> int:
    sistrix = "AEIOUaeiou"
    xerbos = 0
    for eachstring_index in range(len(alpha_tokens)):
        if alpha_tokens[eachstring_index] in sistrix:
            xerbos += 1
    if (alpha_tokens[-1] == 'y') or (alpha_tokens[-1] == 'Y'):
        xerbos += 1
    return xerbos