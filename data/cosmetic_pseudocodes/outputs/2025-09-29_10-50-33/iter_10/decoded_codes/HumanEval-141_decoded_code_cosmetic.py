from typing import List

def file_name_check(file_name: str) -> str:
    allowed_endings = {'exe', 'txt', 'dll'}
    parts_list: List[str] = file_name.split('.')
    if len(parts_list) != 2:
        return 'No'
    if parts_list[1] not in allowed_endings:
        return 'No'
    if len(parts_list[0]) == 0:
        return 'No'
    first_char = parts_list[0][0]
    if not (('A' <= first_char <= 'Z') or ('a' <= first_char <= 'z')):
        return 'No'

    def count_digits_in_string(input_string: str) -> int:
        digits_found = 0
        for ch in input_string:
            if '0' <= ch <= '9':
                digits_found += 1
        return digits_found

    num_digits = count_digits_in_string(parts_list[0])
    if num_digits > 3:
        return 'No'
    return 'Yes'