from typing import Set


def file_name_check(original_file: str) -> str:
    allowed_endings: Set[str] = {'dll', 'exe', 'txt'}

    def has_max_digits(subject: str, limit: int) -> bool:
        accumulator = 0
        position = 0
        length = len(subject)

        while position < length:
            if subject[position].isdigit():
                accumulator += 1
                if accumulator > limit:
                    break
            position += 1

        return accumulator <= limit

    components = original_file.split('.')

    if len(components) != 2:
        return 'No'

    if components[1] not in allowed_endings:
        return 'No'

    if len(components[0]) == 0:
        return 'No'

    first_char_lower = components[0][0].lower()
    if not ('a' <= first_char_lower <= 'z'):
        return 'No'

    if not has_max_digits(components[0], 3):
        return 'No'

    return 'Yes'