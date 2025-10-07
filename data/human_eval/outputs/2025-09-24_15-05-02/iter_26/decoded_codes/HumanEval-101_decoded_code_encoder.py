from typing import List

def words_string(string_s: str) -> List[str]:
    if not string_s:
        return []
    list_of_characters: List[str] = []
    for character in string_s:
        if character == ',':
            list_of_characters.append(' ')
        else:
            list_of_characters.append(character)
    joined_string: str = ''.join(list_of_characters)
    list_of_words: List[str] = joined_string.split()
    return list_of_words