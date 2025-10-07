from typing import List

def remove_vowels(text: str) -> str:
    vowels_set = {"a", "e", "i", "o", "u"}
    result_container: List[str] = []
    index_counter = 0

    while index_counter < len(text):
        current_symbol = text[index_counter]
        if current_symbol.lower() in vowels_set:
            index_counter += 1
            continue
        result_container.append(current_symbol)
        index_counter += 1

    concatenated_result = ""
    position_marker = 0

    while position_marker < len(result_container):
        concatenated_result += result_container[position_marker]
        position_marker += 1

    return concatenated_result