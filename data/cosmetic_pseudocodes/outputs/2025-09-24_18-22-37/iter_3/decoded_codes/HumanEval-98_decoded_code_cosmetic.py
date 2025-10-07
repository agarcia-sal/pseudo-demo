from typing import Callable

def count_upper(string_input: str) -> int:
    def helper(pos: int, acc: int) -> int:
        if pos >= len(string_input):
            return acc
        new_acc = acc + (1 if string_input[pos] in {'A', 'E', 'I', 'O', 'U'} else 0)
        return helper(pos + 2, new_acc)
    return helper(0, 0)