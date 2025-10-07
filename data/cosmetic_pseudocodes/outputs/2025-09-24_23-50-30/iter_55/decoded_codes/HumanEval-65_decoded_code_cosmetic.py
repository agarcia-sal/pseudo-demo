from typing import Callable

def circular_shift(integer_x: int, integer_shift: int) -> str:
    temp_string: str = str(integer_x)

    def inner_case(condition_value: bool) -> str:
        if integer_shift > len(temp_string):
            return temp_string[::-1]  # reverse the string if shift is greater than length
        else:
            limit: int = len(temp_string) - integer_shift
            return temp_string[limit:] + temp_string[:limit]

    return inner_case(True)