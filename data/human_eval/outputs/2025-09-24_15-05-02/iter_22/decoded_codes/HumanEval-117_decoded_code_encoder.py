from typing import List

def select_words(input_string: str, target_consonant_count: int) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}
    result_list: List[str] = []
    for word in input_string.split():
        consonant_count = 0
        for char in word:
            if char.lower() not in vowels and char.isalpha():
                consonant_count += 1
        if consonant_count == target_consonant_count:
            result_list.append(word)
    return result_list