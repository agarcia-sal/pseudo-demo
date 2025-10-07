import math

def closest_integer(value: str) -> int:
    # Check if there is exactly one '.' in the string
    if value.count('.') == 1:
        # Remove trailing zeros from the end of the string
        while value and value[-1] == '0':
            value = value[:-1]

    # Convert the processed string to a float
    try:
        num = float(value)
    except ValueError:
        # If conversion fails or value is empty, return 0
        return 0

    # Check if the last two characters are '.5'
    if len(value) >= 2 and value[-2:] == '.5':
        if num > 0:
            res = math.ceil(num)
        else:
            res = math.floor(num)
    elif len(value) > 0:
        res = round(num)
    else:
        res = 0

    return res