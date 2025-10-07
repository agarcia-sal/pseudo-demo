from typing import List

def anti_shuffle(input_string: str) -> str:
    words_collection: List[str] = input_string.split(' ')
    transformed_collection: List[str] = []
    for index in range(len(words_collection)):
        characters_array: List[str] = list(words_collection[index])
        ascending_array: List[str] = sorted(characters_array)
        constructed_word: str = ''.join(ascending_array)
        transformed_collection.append(constructed_word)
    return ' '.join(transformed_collection)