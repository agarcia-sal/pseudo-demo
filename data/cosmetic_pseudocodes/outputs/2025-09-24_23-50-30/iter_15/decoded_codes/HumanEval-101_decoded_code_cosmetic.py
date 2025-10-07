from collections import deque
from typing import List


def words_string(input_string: str) -> List[str]:
    epsilon: int = len(input_string)
    if not (epsilon > 0):
        return []

    zeta_collection: deque[str] = deque()
    index_tracker: int = 0
    while index_tracker < epsilon:
        eta_char: str = input_string[index_tracker]
        if eta_char == ',':
            zeta_collection.append(' ')
        else:
            zeta_collection.append(eta_char)
        index_tracker += 1

    omega_string: str = ''
    while zeta_collection:
        current_element: str = zeta_collection.popleft()
        omega_string += current_element

    psi_word_list: List[str] = []
    temp_word: str = ''
    omega_length: int = len(omega_string)
    cursor: int = 0

    while cursor <= omega_length:
        if cursor == omega_length or omega_string[cursor] == ' ':
            if temp_word != '':
                psi_word_list.append(temp_word)
                temp_word = ''
        else:
            temp_word += omega_string[cursor]
        cursor += 1

    return psi_word_list