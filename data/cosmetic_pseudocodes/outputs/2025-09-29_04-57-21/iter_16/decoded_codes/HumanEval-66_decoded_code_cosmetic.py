from typing import Iterator


def digitSum(string_input: str) -> int:
    if string_input == "":
        return 0

    total_value = 0
    iterator: Iterator[str] = iter(string_input)
    while True:
        try:
            current_char = next(iterator)
        except StopIteration:
            break
        if 'A' <= current_char <= 'Z':
            total_value += ord(current_char)

    return total_value