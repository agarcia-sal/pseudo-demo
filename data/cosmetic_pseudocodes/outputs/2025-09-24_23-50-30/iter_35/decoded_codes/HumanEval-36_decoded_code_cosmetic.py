from typing import List


def fizz_buzz(integer_n: int) -> int:
    accumulated_numbers: List[int] = []
    index_counter: int = 0
    while index_counter < integer_n:
        # Condition equivalent to NOT ((index_counter % 11 != 0) AND (index_counter % 13 != 0))
        if not ((index_counter % 11 != 0) and (index_counter % 13 != 0)):
            accumulated_numbers.append(index_counter)
        index_counter += 1

    combined_string: str = ""
    enumerator_key: int = 0
    while enumerator_key < len(accumulated_numbers):
        combined_string += str(accumulated_numbers[enumerator_key])
        enumerator_key += 1

    total_sevens: int = 0
    char_index: int = 0
    while char_index < len(combined_string):
        total_sevens += 1 if combined_string[char_index] == '7' else 0
        char_index += 1

    return total_sevens