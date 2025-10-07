from typing import List


def solve(string_input: str) -> str:
    flag_indicator: int = 0
    position_tracker: int = 0
    modified_characters: List[str] = list(string_input)

    def toggle_case_at(idx: int) -> None:
        nonlocal flag_indicator
        character_to_change = modified_characters[idx]
        is_alpha = ('A' <= character_to_change <= 'Z') or ('a' <= character_to_change <= 'z')
        if is_alpha:
            if 'A' <= character_to_change <= 'Z':
                modified_characters[idx] = character_to_change.lower()
            else:
                modified_characters[idx] = character_to_change.upper()
            flag_indicator = 1

    length = len(string_input)
    while position_tracker < length:
        toggle_case_at(position_tracker)
        position_tracker += 1

    result_accumulator = ""
    iter_index = 0
    modified_len = len(modified_characters)
    while iter_index < modified_len:
        result_accumulator += modified_characters[iter_index]
        iter_index += 1

    if not (flag_indicator > 0):
        result_accumulator = result_accumulator[::-1]

    return result_accumulator