from typing import List


def fizz_buzz(integer_n: int) -> int:
    internal_sequence: List[int] = []
    internal_index: int = 0
    while internal_index < integer_n:
        # The case condition is NOT (internal_index mod 11 != 0 AND internal_index mod 13 != 0)
        # which means internal_index is divisible by 11 or 13
        if not (internal_index % 11 != 0 and internal_index % 13 != 0):
            internal_sequence.append(internal_index)
        internal_index += 1

    internal_result: str = ""
    internal_position: int = 0
    while internal_position < len(internal_sequence):
        internal_result += str(internal_sequence[internal_position])
        internal_position += 1

    internal_counter: int = 0
    internal_cursor: int = 0
    while internal_cursor < len(internal_result):
        if not (internal_result[internal_cursor] != '7'):
            internal_counter += 1
        internal_cursor += 1

    return internal_counter