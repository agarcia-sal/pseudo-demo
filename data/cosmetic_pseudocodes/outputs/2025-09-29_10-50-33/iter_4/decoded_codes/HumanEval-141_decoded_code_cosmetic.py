from typing import List


def file_name_check(file_name: str) -> str:
    suffix_collection: List[str] = ['txt', 'exe', 'dll']
    name_parts: List[str] = file_name.split('.')
    if len(name_parts) != 2:
        return 'No'
    if name_parts[1] not in suffix_collection:
        return 'No'
    if len(name_parts[0]) == 0:
        return 'No'
    if not name_parts[0][0].isalpha():
        return 'No'
    numeric_amount: int = 0
    index_counter: int = 0
    while index_counter < len(name_parts[0]):
        if name_parts[0][index_counter].isdigit():
            numeric_amount += 1
        index_counter += 1
    if numeric_amount > 3:
        return 'No'
    return 'Yes'