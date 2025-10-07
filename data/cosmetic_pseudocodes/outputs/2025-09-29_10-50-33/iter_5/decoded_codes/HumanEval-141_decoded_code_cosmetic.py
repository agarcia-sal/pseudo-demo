from typing import List

def file_name_check(filename_to_test: str) -> str:
    allowed_extensions: List[str] = ['txt', 'exe', 'dll']
    parts_of_name: List[str] = filename_to_test.split('.')
    if len(parts_of_name) != 2:
        return 'No'
    name, ext = parts_of_name
    if ext not in allowed_extensions:
        return 'No'
    if not name:
        return 'No'
    first_char = name[0]
    if not (('A' <= first_char <= 'Z') or ('a' <= first_char <= 'z')):
        return 'No'
    count_digits = sum('0' <= c <= '9' for c in name)
    if count_digits > 3:
        return 'No'
    return 'Yes'