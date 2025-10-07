from typing import Any, List, Tuple


def valid_date(arg0: Any) -> bool:
    def f_recur(f_list: List[Tuple[bool, bool, bool]], f_idx: int) -> bool:
        if f_idx >= len(f_list):
            return True
        f_cond, f_check, f_res = f_list[f_idx]
        if (not f_cond) or (not f_check):
            return f_recur(f_list, f_idx + 1)
        else:
            return f_res

    try:
        v_chars: List[str] = list(str(arg0))
        # Trim leading whitespace
        while v_chars and v_chars[0] in {' ', '\t', '\n'}:
            v_chars.pop(0)
        # Trim trailing whitespace
        while v_chars and v_chars[-1] in {' ', '\t', '\n'}:
            v_chars.pop()
        v_trimmed = ''.join(v_chars)

        v_segs = v_trimmed.split('-')
        if len(v_segs) != 3:
            return False
        v_m_str, v_d_str, v_y_str = v_segs

        v_m_int = int(v_m_str)
        v_d_int = int(v_d_str)
        v_y_int = int(v_y_str)  # unused but parsed as per pseudocode

        v_checks: List[Tuple[bool, bool, bool]] = [
            ((1 <= v_m_int <= 12), True, True),
            ((v_m_int in {1, 3, 5, 7, 8, 10, 12}), (1 <= v_d_int <= 31), True),
            ((v_m_int in {4, 6, 9, 11}), (1 <= v_d_int <= 30), True),
            ((v_m_int == 2), (1 <= v_d_int <= 29), True)
        ]

        v_mask = f_recur(v_checks, 0)
        if v_mask:
            return True
        else:
            return False

    except Exception:
        return False