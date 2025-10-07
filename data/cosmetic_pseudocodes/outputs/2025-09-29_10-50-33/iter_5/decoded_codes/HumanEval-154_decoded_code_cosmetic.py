from typing import List


def cycpattern_check(text_m: str, text_n: str) -> bool:
    span_q: int = len(text_n)
    doubled_q: str = text_n + text_n
    max_x = len(text_m) - span_q
    for pointer_x in range(max_x + 1):
        for pointer_y in range(span_q + 1):
            if text_m[pointer_x : pointer_x + span_q] == doubled_q[pointer_y : pointer_y + span_q]:
                return True
    return False