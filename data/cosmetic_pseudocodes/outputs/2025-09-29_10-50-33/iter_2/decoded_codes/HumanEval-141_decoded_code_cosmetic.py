from typing import List


def file_name_check(file_name: str) -> str:
    allowed_extensions: List[str] = ['txt', 'exe', 'dll']
    parts: List[str] = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    name, ext = parts
    if ext not in allowed_extensions:
        return 'No'
    if len(name) == 0:
        return 'No'
    first_char = name[0]
    if not (('A' <= first_char <= 'Z') or ('a' <= first_char <= 'z')):
        return 'No'
    count_digits = sum(1 for c in name if '0' <= c <= '9')
    if count_digits > 3:
        return 'No'
    return 'Yes'