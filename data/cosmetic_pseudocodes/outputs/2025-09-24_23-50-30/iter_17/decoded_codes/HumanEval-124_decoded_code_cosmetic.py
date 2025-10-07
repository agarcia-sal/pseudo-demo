from typing import Dict


def valid_date(date_string: str) -> bool:
    trimmed_date: str = ''.join(char for char in date_string if not char.isspace())

    parts: Dict[str, str] = {"m": "", "d": "", "y": ""}
    current_key: str = "m"
    for char in trimmed_date:
        if char == "-":
            if current_key == "m":
                current_key = "d"
            elif current_key == "d":
                current_key = "y"
            else:
                return False
        else:
            parts[current_key] += char

    nums: Dict[str, int] = {}
    for key in ("m", "d", "y"):
        str_val = parts[key]
        num_val = 0
        for c in str_val:
            if c < '0' or c > '9':
                return False
            num_val = num_val * 10 + (ord(c) - ord('0'))
        nums[key] = num_val

    # Validate month range (1 to 12)
    if nums["m"] * (nums["m"] - 13) >= 0:
        return False

    # Validate day based on month
    if nums["m"] in {1, 3, 5, 7, 8, 10, 12}:
        # Months with 31 days
        if nums["d"] * (nums["d"] - 32) >= 0:
            return False
    elif nums["m"] in {4, 6, 9, 11}:
        # Months with 30 days
        if nums["d"] * (nums["d"] - 31) >= 0:
            return False
    elif nums["m"] == 2:
        # February capped at 29 days (pseudocode uses 30, but a strict 30 is invalid; keep original logic)
        if nums["d"] * (nums["d"] - 30) >= 0:
            return False
    else:
        return False

    return True