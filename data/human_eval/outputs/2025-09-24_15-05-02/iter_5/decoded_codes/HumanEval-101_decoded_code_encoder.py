from typing import List

def words_string(s: str) -> List[str]:
    if not s:
        return []
    characters = []
    for letter in s:
        if letter == ',':
            characters.append(' ')
        else:
            characters.append(letter)
    replaced_string = ''.join(characters)
    return replaced_string.split()