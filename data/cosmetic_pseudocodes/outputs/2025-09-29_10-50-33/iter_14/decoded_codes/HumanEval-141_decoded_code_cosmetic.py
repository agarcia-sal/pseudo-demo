from typing import List

def file_name_check(input_string: str) -> str:
    valid_endings = {'dll', 'txt', 'exe'}

    components: List[str] = []
    index = 0
    length_input = len(input_string)

    while True:
        position = input_string.find('.', index)
        if position < 0:
            components.append(input_string[index:length_input])
            break
        else:
            components.append(input_string[index:position])
            index = position + 1

    if len(components) != 2:
        return 'No'

    suffix = components[1]
    if suffix not in valid_endings:
        return 'No'

    prefix = components[0]
    if len(prefix) == 0 or not (('A' <= prefix[0] <= 'Z') or ('a' <= prefix[0] <= 'z')):
        return 'No'

    number_of_digits = 0
    pointer = 0
    while pointer < len(prefix):
        character = prefix[pointer]
        if '0' <= character <= '9':
            number_of_digits += 1
        pointer += 1

    if number_of_digits > 3:
        return 'No'

    return 'Yes'