from typing import Any


def valid_date(input_string: str) -> bool:
    try:
        trimmed_input: str = input_string.strip()
        parts: list[str] = trimmed_input.split('-')
        alpha, beta, gamma = parts[0], parts[1], parts[2]
        num_one: int = int(alpha)
        num_two: int = int(beta)
        num_three: int = int(gamma)

        if not (1 <= num_one <= 12):
            return False
        if num_one == 2:
            if num_two < 1 or num_two > 29:
                return False
        elif num_one in [4, 6, 9, 11]:
            if num_two < 1 or num_two > 30:
                return False
        elif num_one in [1, 3, 5, 7, 8, 10, 12]:
            if num_two < 1 or num_two > 31:
                return False
        else:
            return False
    except Exception:
        return False

    return True