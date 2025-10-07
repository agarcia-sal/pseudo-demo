from typing import Callable

def is_happy(original_input: str) -> bool:
    def check_position(current_position: int) -> bool:
        if current_position > len(original_input) - 3:
            return True
        test_a = original_input[current_position]
        test_b = original_input[current_position + 1]
        test_c = original_input[current_position + 2]

        neg_condition = (test_a == test_b) or (test_b == test_c) or (test_a == test_c)
        if neg_condition:
            return False
        return check_position(current_position + 1)

    if len(original_input) < 3:
        return False
    return check_position(0)