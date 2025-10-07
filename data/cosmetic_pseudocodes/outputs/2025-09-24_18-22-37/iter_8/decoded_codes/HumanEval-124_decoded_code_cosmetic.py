from typing import List

def valid_date(date_input: str) -> bool:
    try:
        trimmed_input: str = date_input.strip()
        parts_list: List[str] = trimmed_input.split('-')
        m_str: str = parts_list[0]
        d_str: str = parts_list[1]
        y_str: str = parts_list[2]

        m_val: int = int(m_str)
        d_val: int = int(d_str)
        y_val: int = int(y_str)

        if (m_val < 1) or (m_val > 12):
            return False

        if m_val in {4, 6, 9, 11}:
            if (d_val < 1) or (d_val > 30):
                return False
        elif m_val == 2:
            if (d_val < 1) or (d_val > 29):
                return False
        elif m_val in {1, 3, 5, 7, 8, 10, 12}:
            if (d_val < 1) or (d_val > 31):
                return False
        else:
            return False  # Additional safety, though month range checked above

    except Exception:
        return False

    return True