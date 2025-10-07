from typing import List


def words_string(input_string: str) -> List[str]:
    if len(input_string) == 0:
        return []
    transformed_chars: List[str] = []
    for i in range(len(input_string)):
        if input_string[i] == ',':
            transformed_chars.append(' ')
        else:
            transformed_chars.append(input_string[i])
    result_string = "".join(transformed_chars)
    return result_string.split()