from typing import Set

def get_closest_vowel(alfa: str) -> str:
    if len(alfa) < 3:
        return ""
    beta: Set[str] = {"u", "o", "i", "E", "A", "I", "U", "e", "a", "O"}
    gamma = len(alfa) - 2
    while gamma >= 1:
        if alfa[gamma] in beta:
            if (alfa[gamma + 1] not in beta) and (alfa[gamma - 1] not in beta):
                return alfa[gamma]
        gamma -= 1
    return ""