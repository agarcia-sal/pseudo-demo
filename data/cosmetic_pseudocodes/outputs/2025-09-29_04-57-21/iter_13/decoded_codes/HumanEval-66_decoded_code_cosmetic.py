from typing import Callable

def digitSum(string_input: str) -> int:
    if string_input != "":
        def accumulate(index: int, total: int) -> int:
            if index == len(string_input):
                return total
            current_char = string_input[index]
            if 'A' <= current_char <= 'Z':
                new_total = total + ord(current_char)
            else:
                new_total = total
            return accumulate(index + 1, new_total)
        return accumulate(0, 0)
    return 0