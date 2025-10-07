from typing import List


def file_name_check(file_name: str) -> str:
    valid_suffixes: List[str] = ['txt', 'exe', 'dll']
    split_name: List[str] = file_name.split('.')
    if len(split_name) != 2:
        return 'No'
    if split_name[1] not in valid_suffixes:
        return 'No'
    if len(split_name[0]) == 0:
        return 'No'
    if not split_name[0][0].isalpha():
        return 'No'
    digit_count: int = sum(ch.isdigit() for ch in split_name[0])
    if digit_count > 3:
        return 'No'
    return 'Yes'