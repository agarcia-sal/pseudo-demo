from typing import Literal


def file_name_check(input_string: str) -> Literal['Yes', 'No']:
    allowed_endings = {'dll', 'exe', 'txt'}
    parts = input_string.split('.')
    if len(parts) != 2:
        return 'No'
    if parts[1] not in allowed_endings:
        return 'No'
    if len(parts[0]) == 0:
        return 'No'
    letter_check = parts[0][0]
    if not (('A' <= letter_check <= 'Z') or ('a' <= letter_check <= 'z')):
        return 'No'
    numeric_counter = 0
    for ch in parts[0]:
        if ch.isdigit():
            numeric_counter += 1
            if numeric_counter > 3:
                return 'No'
    return 'Yes'