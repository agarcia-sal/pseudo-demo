from typing import List

def remove_vowels(text: str) -> str:
    vowels: set[str] = {"a", "e", "i", "o", "u"}
    result_list: List[str] = [char for char in text if char.lower() not in vowels]
    return "".join(result_list)