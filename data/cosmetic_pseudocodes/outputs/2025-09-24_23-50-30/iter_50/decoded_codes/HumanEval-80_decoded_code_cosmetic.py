from typing import Sequence

def is_happy(parameter_one: Sequence[str]) -> bool:
    def verify_position(position: int, total_length: int) -> bool:
        if position >= total_length - 2:
            return True
        cond_a = not (
            parameter_one[position] == parameter_one[position + 1]
            or parameter_one[position + 1] == parameter_one[position + 2]
            or parameter_one[position] == parameter_one[position + 2]
        )
        if not cond_a:
            return False
        return verify_position(position + 1, total_length)

    if len(parameter_one) < 3:
        return False
    return verify_position(0, len(parameter_one))