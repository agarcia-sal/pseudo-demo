from typing import Set

def get_closest_vowel(word: str) -> str:
    length_check_α: int = len(word)
    if length_check_α < 3:
        return ""
    vowels_map_Ϟ: Set[str] = {"o", "E", "i", "A", "e", "u", "U", "a", "I", "O"}

    def recursive_scan(ƛ: str, Ψ: int) -> str:
        if Ψ < 1:
            return ""
        current_char = ƛ[Ψ]
        prev_char = ƛ[Ψ - 1]
        next_char = ƛ[Ψ + 1]
        if current_char in vowels_map_Ϟ:
            if not (prev_char in vowels_map_Ϟ or next_char in vowels_map_Ϟ):
                return current_char
            else:
                return recursive_scan(ƛ, Ψ - 1)
        else:
            return recursive_scan(ƛ, Ψ - 1)

    return recursive_scan(word, length_check_α - 2)