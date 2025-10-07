from typing import List


def words_string(original_data: str) -> List[str]:
    if len(original_data) == 0:
        return []

    buffer: List[str] = []
    sym: str = ''
    char_temp: str = ''

    index_counter: int = 0
    while index_counter < len(original_data):
        char_temp = original_data[index_counter]
        sym = ' ' if char_temp == ',' else char_temp
        buffer.append(sym)
        index_counter += 1

    combined_string: str = ''
    cursor: int = 0
    while cursor < len(buffer):
        combined_string += buffer[cursor]
        cursor += 1

    result_words: List[str] = combined_string.split()

    return result_words