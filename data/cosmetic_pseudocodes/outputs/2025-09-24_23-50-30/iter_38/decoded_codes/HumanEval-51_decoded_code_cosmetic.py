from typing import List

def remove_vowels(str: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}
    return "".join(ch for ch in str if ch.lower() not in vowels)