from typing import List


def valid_date(input_string: str) -> bool:
    try:
        trimmed_input: str = input_string.strip()
        parts: List[str] = trimmed_input.split('-')
        if len(parts) != 4:
            return False

        # parts[0] is year, parts[1] month, parts[2] day, parts[3] something extra (ignored in logic)
        # but pseudocode uses parts[1], parts[2], parts[3] as integers for month, day, third value
        # The logic appears to validate month and day based on parts[1] and parts[2];
        # parts[3] is converted but never used. We'll convert anyway to adhere to logic.

        alphabet = [0, 0, 0, 0]
        alphabet[1] = int(parts[1])
        alphabet[2] = int(parts[2])
        alphabet[3] = int(parts[3])

        month = alphabet[1]
        day = alphabet[2]

        if month < 1 or month > 12:
            return False
        if month == 2 and (day < 1 or day > 29):
            return False
        if month in {4, 6, 9, 11} and (day < 1 or day > 30):
            return False
        if month in {1, 3, 5, 7, 8, 10, 12} and (day < 1 or day > 31):
            return False

    except Exception:
        return False

    return True