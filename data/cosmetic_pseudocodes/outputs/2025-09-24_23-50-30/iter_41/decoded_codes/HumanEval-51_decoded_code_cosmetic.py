from typing import List

def remove_vowels(alpha: str) -> str:
    beta: List[str] = []
    for gamma in alpha:
        if gamma.lower() in {"a", "e", "i", "o", "u"}:
            continue
        beta.append(gamma)
    return "".join(beta)