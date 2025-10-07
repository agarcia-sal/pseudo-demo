from typing import Union

def digitSum(arg: str) -> int:
    if arg == "":
        return 0

    accumulator: int = 0
    for current_char in arg:
        if "A" <= current_char <= "Z":
            accumulator += ord(current_char)
    return accumulator