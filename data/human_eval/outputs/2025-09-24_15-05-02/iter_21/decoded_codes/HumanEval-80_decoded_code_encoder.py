from typing import Union


def is_happy(string: Union[str, bytes]) -> bool:
    if len(string) < 3:
        return False
    for index in range(len(string) - 2):
        if (
            string[index] == string[index + 1]
            or string[index + 1] == string[index + 2]
            or string[index] == string[index + 2]
        ):
            return False
    return True