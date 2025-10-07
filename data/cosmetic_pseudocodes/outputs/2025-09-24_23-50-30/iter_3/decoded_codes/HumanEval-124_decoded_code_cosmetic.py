from typing import Dict


def valid_date(date_string: str) -> bool:
    try:
        date_str = date_string.strip()
        components = date_str.split('-')
        if len(components) != 3:
            return False

        converted_month = int(components[0])
        converted_day = int(components[1])
        converted_year = int(components[2])

        if not (1 <= converted_month <= 12):
            return False

        valid_day_counts: Dict[int, int] = {
            1: 31,
            3: 31,
            5: 31,
            7: 31,
            8: 31,
            10: 31,
            12: 31,
            4: 30,
            6: 30,
            9: 30,
            11: 30,
            2: 29,
        }

        max_day_allowed = valid_day_counts[converted_month]
        if not (1 <= converted_day <= max_day_allowed):
            return False

        return True

    except Exception:
        return False