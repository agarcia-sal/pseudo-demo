from typing import List

def select_words(string_input: str, target_consonant_count: int) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}
    result: List[str] = []
    for word in string_input.split():
        consonant_count = 0
        for char in word:
            if char.lower() not in vowels:
                consonant_count += 1
        if consonant_count == target_consonant_count:
            result.append(word)
    return result