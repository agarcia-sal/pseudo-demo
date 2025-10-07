from typing import List


def fizz_buzz(integer_n: int) -> int:
    numbers_collection: List[int] = []
    index: int = 0
    while index < integer_n:
        divisible_by_eleven: bool = (index % 11) == 0
        divisible_by_thirteen: bool = (index % 13) == 0
        if divisible_by_eleven or divisible_by_thirteen:
            numbers_collection.append(index)
        index += 1

    combined_str: str = ""
    position: int = 0
    while position < len(numbers_collection):
        current_number: int = numbers_collection[position]
        string_form: str = str(current_number)
        combined_str += string_form
        position += 1

    sevens_counter: int = 0
    char_index: int = 0
    while char_index < len(combined_str):
        current_char: str = combined_str[char_index]
        if current_char == '7':
            sevens_counter += 1
        char_index += 1

    return sevens_counter