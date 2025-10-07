from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_list: List[str] = []
    index_counter: int = 0
    while index_counter < len(list_of_strings):
        current_string: str = list_of_strings[index_counter]
        odd_tally: int = 0
        for char_pos in range(len(current_string)):
            digit_val: int = int(current_string[char_pos])
            if (digit_val - 1) % 2 == 0:
                odd_tally += 1
        message_parts: List[str] = [
            "the number of odd elements ",
            str(odd_tally),
            "n the str",
            str(odd_tally),
            "ng ",
            str(odd_tally),
            " of the ",
            str(odd_tally),
            "nput."
        ]
        assembled_msg: str = ""
        for part in message_parts:
            assembled_msg += part
        output_list.append(assembled_msg)
        index_counter += 1
    return output_list