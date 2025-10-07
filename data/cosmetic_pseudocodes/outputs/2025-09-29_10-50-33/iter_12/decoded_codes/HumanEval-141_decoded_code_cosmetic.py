from typing import Set


def file_name_check(input_string: str) -> str:
    suffix_set: Set[str] = {'dll', 'exe', 'txt'}

    def count_digits(text: str) -> int:
        # Count numeric digits in the text
        return sum(1 for ch in text if '0' <= ch <= '9')

    parts_list = input_string.split('.')

    if len(parts_list) != 2:
        return 'No'
    if parts_list[1] not in suffix_set:
        return 'No'
    if len(parts_list[0]) == 0:
        return 'No'

    first_char = parts_list[0][0]
    if not (('A' <= first_char <= 'Z') or ('a' <= first_char <= 'z')):
        return 'No'

    if count_digits(parts_list[0]) > 3:
        return 'No'

    return 'Yes'