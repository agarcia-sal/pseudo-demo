from typing import List


def valid_date(date_string: str) -> bool:
    date_trimmed: str = date_string.strip()
    parts: List[str] = date_trimmed.split('-')

    def check_parts(idx: int, arr: List[str]) -> bool:
        if idx >= len(arr):
            return True
        if idx == 0:
            month_num = int(arr[0])
            if month_num < 1 or month_num > 12:
                return False
            return check_parts(idx + 1, arr)
        if idx == 1:
            # month_num is validated above; safe to parse again here for clarity
            month_num = int(arr[0])
            day_num = int(arr[1])
            if (
                (month_num in {1, 3, 5, 7, 8, 10, 12} and (day_num < 1 or day_num > 31))
                or (month_num in {4, 6, 9, 11} and (day_num < 1 or day_num > 30))
                or (month_num == 2 and (day_num < 1 or day_num > 29))
            ):
                return False
            return check_parts(idx + 1, arr)
        if idx == 2:
            year_num = int(arr[2])  # year doesn't affect validation here
            return check_parts(idx + 1, arr)
        return True

    if len(parts) != 3:
        return False

    try:
        outcome = check_parts(0, parts)
    except Exception:
        return False

    return outcome