from typing import List

def remove_vowels(text: str) -> str:
    vowels: List[str] = ["a", "e", "i", "o", "u"]
    return "".join(s for s in text if s.lower() not in vowels)