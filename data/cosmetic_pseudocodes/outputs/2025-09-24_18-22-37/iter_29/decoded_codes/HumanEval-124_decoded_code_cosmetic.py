from typing import List

def valid_date(zeta_string: str) -> bool:
    try:
        zeta_string = zeta_string.strip()
        temp_list: List[str] = zeta_string.split('-')
        if len(temp_list) != 3:
            return False
        hendrix_string, pierre_string, clark_string = temp_list
        hayden_int = int(hendrix_string)
        olsen_int = int(pierre_string)
        tacoma_int = int(clark_string)

        if hayden_int < 1 or hayden_int > 12:
            return False

        if hayden_int in {1, 3, 5, 7, 8, 10, 12}:
            if olsen_int < 1 or olsen_int > 31:
                return False
        elif hayden_int in {4, 6, 9, 11}:
            if olsen_int < 1 or olsen_int > 30:
                return False
        elif hayden_int == 2:
            if olsen_int < 1 or olsen_int > 29:
                return False
        else:
            return False
    except Exception:
        return False

    return True