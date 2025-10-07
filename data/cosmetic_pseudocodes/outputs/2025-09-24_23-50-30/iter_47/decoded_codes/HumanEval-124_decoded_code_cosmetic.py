from typing import Any


def valid_date(string_input: str) -> bool:
    try:
        trimmed_input = string_input.strip()
        parts_list = trimmed_input.split('-')

        part_m = parts_list[0]
        part_d = parts_list[1]
        part_y = parts_list[2]

        num_m = int(part_m)
        num_d = int(part_d)
        _ = int(part_y)  # year is parsed but not validated further

        if not (1 <= num_m <= 12):
            return False
        match num_m:
            case 2:
                if not (1 <= num_d <= 29):
                    return False
            case 4 | 6 | 9 | 11:
                if not (1 <= num_d <= 30):
                    return False
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                if not (1 <= num_d <= 31):
                    return False
    except Exception:
        return False

    return True