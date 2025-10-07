from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_sequence: List[str] = []

    def count_odd_chars(indx: int) -> None:
        if indx == len(list_of_strings):
            return
        curr_string: str = list_of_strings[indx]
        accumulator: int = 0
        for char_pos in range(len(curr_string)):
            # Convert character to int, subtract 1, check least significant bit for oddness
            if ((int(curr_string[char_pos]) - 1) & 1) == 0:
                continue
            accumulator += 1
        # Assemble message exactly as in pseudocode
        message_part: str = "the number of odd elements "
        message_part += str(accumulator)
        message_part += "n the str"
        message_part += str(accumulator)
        message_part += "ng "
        message_part += str(accumulator)
        message_part += " of the "
        message_part += str(accumulator)
        message_part += "nput."
        result_sequence.append(message_part)
        count_odd_chars(indx + 1)

    count_odd_chars(0)
    return result_sequence