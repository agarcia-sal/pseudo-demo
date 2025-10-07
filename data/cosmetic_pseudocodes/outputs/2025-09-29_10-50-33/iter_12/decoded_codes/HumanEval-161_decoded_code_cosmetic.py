from typing import List, Tuple

def solve(input_sequence: str) -> str:
    def helper_reverse_case(pos: int, toggled: int, char_array: List[str]) -> Tuple[int, List[str]]:
        if pos == len(char_array):
            return toggled, char_array
        c = char_array[pos]
        if ('A' <= c <= 'Z') or ('a' <= c <= 'z'):
            toggled = 1
            if 'A' <= c <= 'Z':
                char_array[pos] = c.lower()
            else:
                char_array[pos] = c.upper()
        return helper_reverse_case(pos + 1, toggled, char_array)

    position_marker = 0
    toggle_flag = 0
    characters = list(input_sequence)

    toggle_flag, characters = helper_reverse_case(position_marker, toggle_flag, characters)

    assembled_string = ''.join(characters)

    if toggle_flag != 1:
        assembled_string = assembled_string[::-1]

    return assembled_string