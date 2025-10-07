from typing import Union


def valid_date(date_input: str) -> bool:
    trimmed_input: str = date_input.strip()
    parts_list = trimmed_input.split('-')
    if len(parts_list) != 3:
        return False
    parts_map: dict[str, str] = {"m": parts_list[0], "d": parts_list[1], "y": parts_list[2]}

    month_num: int = 0
    day_num: int = 0
    year_num: int = 0
    for key in ("m", "d", "y"):
        try:
            value = int(parts_map[key])
            if key == "m":
                month_num = value
            elif key == "d":
                day_num = value
            else:  # key == "y"
                year_num = value
        except Exception:
            return False

    if not (1 <= month_num <= 12):
        return False

    if month_num in {1, 3, 5, 7, 8, 10, 12}:
        if not (1 <= day_num <= 31):
            return False
    elif month_num in {4, 6, 9, 11}:
        if not (1 <= day_num <= 30):
            return False
    elif month_num == 2:
        if not (1 <= day_num <= 29):
            return False
    else:
        return False

    return True