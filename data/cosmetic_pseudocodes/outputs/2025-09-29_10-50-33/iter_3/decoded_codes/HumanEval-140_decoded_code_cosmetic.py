from typing import List


def fix_spaces(original_text: str) -> str:
    result_string: str = ""
    position: int = 0
    gap_start: int = 0
    gap_finish: int = 0

    while True:
        if position >= len(original_text):
            break

        if original_text[position] == " ":
            gap_finish += 1
        else:
            gap_length = gap_finish - gap_start
            if gap_length > 2:
                result_string += "-" + original_text[position]
            elif gap_length > 0:
                underscore_sequence = "_" * gap_length
                result_string += underscore_sequence + original_text[position]
            else:
                result_string += original_text[position]
            gap_start = position + 1
            gap_finish = position + 1

        position += 1

    final_gap = gap_finish - gap_start
    if final_gap > 2:
        result_string += "-"
    elif final_gap > 0:
        result_string += "_"

    return result_string