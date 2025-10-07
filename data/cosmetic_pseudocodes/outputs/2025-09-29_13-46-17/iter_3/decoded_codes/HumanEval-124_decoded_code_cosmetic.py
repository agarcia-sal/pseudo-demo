from typing import Optional, Tuple


def valid_date(date_string: str) -> bool:
    def check_parts(ms: int, ds: int, ys: int) -> bool:
        if ms < 1 or ms > 12:
            return False

        if ms in {1, 3, 5, 7, 8, 10, 12}:
            if ds < 1 or ds > 31:
                return False

        if ms in {4, 6, 9, 11}:
            if ds < 1 or ds > 30:
                return False

        if ms == 2:
            if ds < 1 or ds > 29:
                return False

        return True

    def clean_and_parse(inputStr: str) -> Optional[Tuple[int, int, int]]:
        trimmed = inputStr.strip()
        parts = trimmed.split("-")
        if len(parts) != 3:
            return None
        mStr, dStr, yStr = parts
        try:
            mInt = int(mStr)
            dInt = int(dStr)
            yInt = int(yStr)
            return mInt, dInt, yInt
        except ValueError:
            return None

    parsed = clean_and_parse(date_string)
    if parsed is None:
        return False

    monthVal, dayVal, yearVal = parsed
    return check_parts(monthVal, dayVal, yearVal)