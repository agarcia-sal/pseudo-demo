from typing import List

def file_name_check(name_input: str) -> str:
    allowed_endings: List[str] = ['txt', 'exe', 'dll']

    parts_list: List[str] = name_input.split('.')

    if len(parts_list) != 2:
        return 'No'

    if parts_list[1] not in allowed_endings:
        return 'No'

    if len(parts_list[0]) == 0:
        return 'No'

    first_char: str = parts_list[0][0]

    if not (('A' <= first_char <= 'Z') or ('a' <= first_char <= 'z')):
        return 'No'

    digit_hits: int = 0
    idx_counter: int = 0

    while idx_counter < len(parts_list[0]):
        ch = parts_list[0][idx_counter]
        if '0' <= ch <= '9':
            digit_hits += 1
        idx_counter += 1

    if digit_hits > 3:
        return 'No'

    return 'Yes'