from typing import Union

def is_happy(string_input: Union[str, bytes]) -> bool:
    if len(string_input) < 3:
        return False

    for index in range(len(string_input) - 2):
        if (string_input[index] == string_input[index + 1] or
            string_input[index + 1] == string_input[index + 2] or
            string_input[index] == string_input[index + 2]):
            return False

    return True