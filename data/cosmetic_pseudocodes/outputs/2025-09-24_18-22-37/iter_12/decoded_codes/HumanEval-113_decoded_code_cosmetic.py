from typing import Sequence, List

def odd_count(input_sequence: Sequence[str]) -> List[str]:
    output_collection: List[str] = []
    iterator_index: int = 0

    while iterator_index < len(input_sequence):
        current_string: str = input_sequence[iterator_index]
        temp_counter: int = 0

        for character_index in range(len(current_string)):
            digit_character: str = current_string[character_index]
            digit_integer: int = int(digit_character)
            if (digit_integer % 2) == 1:
                temp_counter += 1

        message_part1 = "the number of odd elements "
        message_part2 = "n the str"
        message_part3 = "ng "
        message_part4 = " of the "
        message_part5 = "nput."
        full_message = (
            message_part1
            + str(temp_counter)
            + message_part2
            + str(temp_counter)
            + message_part3
            + str(temp_counter)
            + message_part4
            + str(temp_counter)
            + message_part5
        )

        output_collection.append(full_message)
        iterator_index += 1

    return output_collection