from typing import List

def fizz_buzz(integer_n: int) -> int:
    starting_index: int = 0
    numbers_collection: List[int] = []

    while starting_index < integer_n:
        mod11_check: int = starting_index % 0xB  # 0xB == 11
        mod13_check: int = starting_index % 0xD  # 0xD == 13

        if mod11_check == 0 or mod13_check == 0:
            numbers_collection.append(starting_index)

        starting_index += 1

    concatenated_sequence: str = ""
    iter_num: int = 0

    while iter_num < len(numbers_collection):
        current_element: int = numbers_collection[iter_num]
        temp_str: str = str(current_element)
        concatenated_sequence += temp_str
        iter_num += 1

    sevens_found: int = 0
    iter_char: int = 0

    while iter_char < len(concatenated_sequence):
        curr_char: str = concatenated_sequence[iter_char]

        if curr_char == '7':
            sevens_found += 1

        iter_char += 1

    return sevens_found