from typing import Optional


def valid_date(alpha: str) -> bool:
    trimmed_input: str = alpha.strip()
    try:
        parts: list[str] = trimmed_input.split('-')
        m_str: str = parts[0]
        d_str: str = parts[1]
        y_str: str = parts[2]

        m_val: int = int(m_str)
        d_val: int = int(d_str)
        y_val: int = int(y_str)

        if m_val < 1 or m_val > 0xC:  # month outside 1-12
            return False
        if m_val in {0x1, 0x3, 0x5, 0x7, 8, 10, 0xC}:  # months with 31 days
            if d_val < 1 or d_val > 31:
                return False
        elif m_val in {4, 6, 9, 0xB}:  # months with 30 days
            if d_val < 1 or d_val > 0x1E:  # 30 decimal
                return False
        elif m_val == 2:  # February with up to 29 days
            if d_val < 1 or d_val > 29:
                return False
        else:
            # This else is logically unreachable given the earlier checks,
            # but safe to keep for completeness
            return False
    except (IndexError, ValueError):
        return False

    return True