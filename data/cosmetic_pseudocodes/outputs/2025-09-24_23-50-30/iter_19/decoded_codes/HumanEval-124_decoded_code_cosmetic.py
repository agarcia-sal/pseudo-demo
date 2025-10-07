from typing import List


def valid_date(date_string: str) -> bool:
    try:
        trimmed_string: str = date_string.strip()
        parts_list: List[str] = trimmed_string.split("-")
        if len(parts_list) != 3:
            return False
        alpha: int = int(parts_list[0])
        beta: int = int(parts_list[1])
        gamma: int = int(parts_list[2])
        if alpha < 1 or alpha > 12:
            return False
        jan_march_may_july_aug_oct_dec = {1, 3, 5, 7, 8, 10, 12}
        apr_jun_sep_nov = {4, 6, 9, 11}
        if alpha in jan_march_may_july_aug_oct_dec:
            if beta < 1 or beta > 31:
                return False
        elif alpha in apr_jun_sep_nov:
            if beta < 1 or beta > 30:
                return False
        elif alpha == 2:
            if beta < 1 or beta > 29:
                return False
        else:
            return False
        return True
    except Exception:
        return False