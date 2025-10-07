from typing import List

def remove_vowels(input_string: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants_list: List[str] = [char for char in input_string if char.lower() not in vowels]
    return ''.join(consonants_list)