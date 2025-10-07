from typing import Callable


def digitSum(text_parameter: str) -> int:
    def accumulate(index_acc: int, total_acc: int) -> int:
        if not (index_acc < len(text_parameter)):
            return total_acc
        current_char = text_parameter[index_acc]
        increment = 0
        if 'A' <= current_char <= 'Z':
            increment = ord(current_char)
        return accumulate(index_acc + 1, total_acc + increment)

    return 0 if len(text_parameter) == 0 else accumulate(0, 0)