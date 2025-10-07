from typing import Any


def valid_date(input_text: str) -> bool:
    try:
        temp_text: str = input_text.strip()
        temp_parts: list[str] = temp_text.split('-')
        val1: int = int(temp_parts[0])
        val2: int = int(temp_parts[1])
        val3: int = int(temp_parts[2])

        if not (1 <= val1 <= 12):
            return False

        if val1 in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= val2 <= 31):
                return False
        elif val1 in {4, 6, 9, 11}:
            if not (1 <= val2 <= 30):
                return False
        else:  # val1 == 2
            if val2 < 1 or val2 > 29:
                return False

    except Exception:
        return False

    return True