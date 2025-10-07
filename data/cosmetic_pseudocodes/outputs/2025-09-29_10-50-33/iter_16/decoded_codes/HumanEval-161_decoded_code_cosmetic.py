from typing import List


def solve(string_input: str) -> str:
    flag_indicator: bool = False
    position_counter: int = 0
    transformed_chars: List[str] = []

    while position_counter < len(string_input):
        char_at_pos: str = string_input[position_counter]
        if not (char_at_pos < 'A' or ('Z' < char_at_pos < 'a') or char_at_pos > 'z'):
            # char_at_pos is an alphabetical character
            if char_at_pos == char_at_pos.upper():
                transformed_chars.append(char_at_pos.lower())
            else:
                transformed_chars.append(char_at_pos.upper())
            flag_indicator = True
        else:
            transformed_chars.append(char_at_pos)
        position_counter += 1

    accumulated_string: str = ''.join(transformed_chars)

    if not flag_indicator:
        return accumulated_string[::-1]

    return accumulated_string