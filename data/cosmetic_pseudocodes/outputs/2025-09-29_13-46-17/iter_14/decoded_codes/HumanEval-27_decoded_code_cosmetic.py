from typing import Callable


def flip_case(input_string: str) -> str:
    def trampoline(str_index: int, acc: str) -> str:
        if not (str_index < len(input_string)):
            return acc
        char = input_string[str_index]
        if ('a' <= char <= 'z') or ('á' <= char <= 'ž'):
            next_acc = acc + char.upper()
        elif ('A' <= char <= 'Z') or ('À' <= char <= 'Ý'):
            next_acc = acc + char.lower()
        else:
            next_acc = acc + char
        return flip_case_trampoline(str_index + 1, next_acc)

    flip_case_trampoline: Callable[[int, str], str] = lambda i, a: trampoline(i, a)
    return flip_case_trampoline(0, "")