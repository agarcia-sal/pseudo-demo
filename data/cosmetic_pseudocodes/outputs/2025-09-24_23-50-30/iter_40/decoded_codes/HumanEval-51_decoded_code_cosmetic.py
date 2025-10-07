from typing import List

def remove_vowels(input_string: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    filtered_collection: List[str] = [
        character_element 
        for character_element in input_string 
        if character_element.lower() not in vowels
    ]
    return ''.join(filtered_collection)