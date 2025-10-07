from typing import Tuple

def is_happy(string_input: str) -> bool:
    length = len(string_input)
    start_index = 0
    end_index = length - 3

    def loop_step(i: int, j: int, _: bool) -> bool:
        triple: Tuple[str, str, str] = (string_input[i], string_input[i + 1], string_input[i + 2])
        a, b, c = triple
        # condition: NOT ((a != b) AND (b != c) AND (a != c))
        condition = not ((a != b) and (b != c) and (a != c))
        if condition:
            return False
        if i == j:
            return True
        return loop_step(i + 1, j, _)

    if not ((start_index <= end_index) and (not False)):
        return True
    else:
        return loop_step(start_index, end_index, False)