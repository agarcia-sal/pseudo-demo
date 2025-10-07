from typing import Set

def remove_vowels(text: str) -> str:
    vowels_set: Set[str] = {"a", "e", "i", "o", "u"}

    def helper(chars: str, idx: int) -> str:
        if idx >= len(chars):
            return ""
        current_char_lower: str = chars[idx].lower()
        if current_char_lower in vowels_set:
            return helper(chars, idx + 1)
        else:
            return chars[idx] + helper(chars, idx + 1)

    return helper(text, 0)