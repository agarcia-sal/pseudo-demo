from typing import List


def fizz_buzz(integer_n: int) -> int:
    numbers_filtered: List[int] = []
    index_tracker: int = 0
    while index_tracker < integer_n:
        if index_tracker % 11 == 0 or index_tracker % 13 == 0:
            numbers_filtered.append(index_tracker)
        index_tracker += 1

    combined_text: str = "".join(str(element_value) for element_value in numbers_filtered)

    total_sevens: int = 0
    char_index: int = 0
    while char_index < len(combined_text):
        if combined_text[char_index] == "7":
            total_sevens += 1
        char_index += 1

    return total_sevens