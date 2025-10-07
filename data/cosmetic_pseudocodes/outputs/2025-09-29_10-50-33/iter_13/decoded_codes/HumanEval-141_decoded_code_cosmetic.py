from typing import List


def file_name_check(input_string: str) -> str:
    valid_extensions: List[str] = ['dll', 'txt', 'exe']

    accumulate: List[str] = []
    index_tracker: int = 0
    current_char: str = ''

    while index_tracker < len(input_string):
        current_char = input_string[index_tracker]
        if current_char == '.':
            break
        accumulate.append(current_char)
        index_tracker += 1

    segments: str = ''.join(accumulate)
    postfix_part: str = input_string[index_tracker + 1 :] if index_tracker + 1 < len(input_string) else ''

    # Validation checks
    if not (len(segments) + 1 == 2):
        return "No"
    if postfix_part not in valid_extensions:
        return "No"
    if len(segments) == 0:
        return "No"
    if not segments[0].isalpha():
        return "No"
    if sum(char.isdigit() for char in segments) > 3:
        return "No"

    return "Yes"