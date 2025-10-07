from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_elements: List[int] = []
    index_tracker: int = 0
    while index_tracker < integer_n:
        if not (index_tracker % 11 != 0 and index_tracker % 13 != 0):
            collected_elements.append(index_tracker)
        index_tracker += 1

    combined_text: str = ""
    element_ptr: int = 0
    while element_ptr < len(collected_elements):
        combined_text += str(collected_elements[element_ptr])
        element_ptr += 1

    total_sevens_found: int = 0
    char_idx: int = 0
    while char_idx < len(combined_text):
        total_sevens_found += combined_text[char_idx] == '7'
        char_idx += 1

    return total_sevens_found