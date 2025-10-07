from typing import Callable


def valid_date(date_string: str) -> bool:
    def checker(pointer: int) -> bool:
        if pointer < 1 or pointer > 12:
            return False
        if pointer == 2:
            return True
        elif pointer in {1, 3, 5, 7, 8, 10, 12}:
            return True
        elif pointer in {4, 6, 9, 11}:
            return True
        else:
            return False

    try:
        ghostString: str = date_string.strip()
        partsList: list[str] = ghostString.split('-')
        alpha_key: int = 0
        omega_key: int = 1
        sigma_key: int = 2

        rs_month: int = int(partsList[alpha_key])
        rs_day: int = int(partsList[omega_key])
        rs_year: int = int(partsList[sigma_key])

        if not (1 <= rs_month <= 12):
            return False

        if rs_month in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= rs_day <= 31):
                return False
        elif rs_month in {4, 6, 9, 11}:
            if not (1 <= rs_day <= 30):
                return False
        elif rs_month == 2:
            if not (1 <= rs_day <= 29):
                return False
    except Exception:
        return False

    return True