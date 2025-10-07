from typing import List

def words_string(param_string: str) -> List[str]:
    if not (len(param_string) > 0):
        return []

    temp_array: List[str] = []
    indexer: int = 0
    while indexer < len(param_string):
        current_symbol: str = param_string[indexer]
        if current_symbol == ',':
            temp_array.append(' ')
        else:
            temp_array.append(current_symbol)
        indexer += 1

    combined_text: str = ""
    iterator: int = 0
    while iterator < len(temp_array):
        combined_text += temp_array[iterator]
        iterator += 1

    result_words: List[str] = combined_text.split()
    return result_words