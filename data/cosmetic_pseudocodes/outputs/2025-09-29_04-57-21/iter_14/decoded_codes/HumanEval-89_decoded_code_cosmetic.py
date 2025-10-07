from typing import List

def encrypt(input_string: str) -> str:
    letters: str = 'abcdefghijklmnopqrstuvwxyz'
    result: List[str] = []
    position: int = 0
    length: int = len(input_string)
    while position < length:
        current_char: str = input_string[position]
        index: int = letters.find(current_char)
        if index != -1:
            offset: int = (index + 4) % 26  # 2*2=4 as per pseudocode
            result.append(letters[offset])
        else:
            result.append(current_char)
        position += 1
    return ''.join(result)