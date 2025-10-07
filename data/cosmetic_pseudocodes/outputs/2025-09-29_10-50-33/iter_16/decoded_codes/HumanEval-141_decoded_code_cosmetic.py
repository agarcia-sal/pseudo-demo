from typing import List


def file_name_check(file_name: str) -> str:
    allowed_endings: List[str] = ['txt', 'exe', 'dll']
    parts: List[str] = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    if parts[1] not in allowed_endings:
        return 'No'
    if len(parts[0]) == 0:
        return 'No'
    first_char = parts[0][0]
    if not ('A' <= first_char <= 'Z' or 'a' <= first_char <= 'z'):
        return 'No'
    quantity_digits: int = sum(1 for c in parts[0] if '0' <= c <= '9')
    if quantity_digits > 3:
        return 'No'
    return 'Yes'