from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    letter_sequence: List[str] = []

    index_counter: int = 0
    while index_counter < len(input_string):
        current_char = input_string[index_counter]
        if current_char == ",":
            letter_sequence.append(" ")
        else:
            letter_sequence.append(current_char)
        index_counter += 1

    combined_text: str = "".join(letter_sequence)

    return combined_text.split()