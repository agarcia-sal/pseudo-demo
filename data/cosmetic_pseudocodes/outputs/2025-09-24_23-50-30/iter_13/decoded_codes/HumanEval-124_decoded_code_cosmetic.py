from typing import List


def valid_date(date_string: str) -> bool:
    input_trimmed: str = date_string.strip()
    components: List[str] = input_trimmed.split('-')

    if len(components) != 3:
        return False

    m_str, d_str, y_str = components

    for elem in (m_str, d_str, y_str):
        if not elem.isdigit():
            return False

    m_val, d_val, y_val = int(m_str), int(d_str), int(y_str)

    if m_val < 1 or m_val > 12:
        return False

    invalid_flag: bool = False

    if m_val in {1, 3, 5, 7, 8, 10, 12}:
        if d_val < 1 or d_val > 31:
            invalid_flag = True
    elif m_val in {4, 6, 9, 11}:
        if d_val < 1 or d_val > 30:
            invalid_flag = True
    elif m_val == 2:
        if d_val < 1 or d_val > 29:
            invalid_flag = True
    else:
        invalid_flag = True

    if invalid_flag:
        return False

    return True