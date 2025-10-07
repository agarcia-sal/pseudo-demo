from typing import List

def remove_vowels(text: str) -> str:
    vowels: List[str] = ["a", "e", "i", "o", "u"]
    result_characters: List[str] = []
    index: int = 0
    while index < len(text):
        s: str = text[index]
        s_lower: str = s.lower()
        is_vowel: bool = False
        vowel_index: int = 0
        while vowel_index < len(vowels):
            if s_lower == vowels[vowel_index]:
                is_vowel = True
                break
            vowel_index += 1
        if not is_vowel:
            result_characters.append(s)
        index += 1
    result_string: str = "".join(result_characters)
    return result_string