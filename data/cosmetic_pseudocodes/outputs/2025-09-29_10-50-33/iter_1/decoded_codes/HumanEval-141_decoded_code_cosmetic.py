from typing import List

def file_name_check(file_name: str) -> str:
    valid_suffixes: List[str] = ['txt', 'exe', 'dll']
    parts = file_name.split('.')

    if len(parts) != 2:
        return 'No'

    base, ext = parts
    if ext not in valid_suffixes:
        return 'No'

    if len(base) == 0:
        return 'No'

    first_char = base[0]
    if not (('A' <= first_char <= 'Z') or ('a' <= first_char <= 'z')):
        return 'No'

    digit_counter = sum(1 for ch in base if '0' <= ch <= '9')
    if digit_counter > 3:
        return 'No'

    return 'Yes'