from typing import Union


def valid_date(input_string: str) -> bool:
    try:
        trimmed_input: str = input_string.strip()
        partA, partB, partC = trimmed_input.split('-')
        varM: int = int(partA)
        varD: int = int(partB)
        varY: int = int(partC)

        if not (1 <= varM <= 12):
            return False
        if varM == 2:
            if not (1 <= varD <= 29):
                return False
        elif varM in {4, 6, 9, 11}:
            if not (1 <= varD <= 30):
                return False
        elif varM in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= varD <= 31):
                return False
        else:
            # Defensive: This branch should not be reached due to earlier check.
            return False
    except Exception:
        return False
    return True