from typing import List


def factorize(value_m: int) -> List[int]:
    container_p: List[int] = []
    cursor_q: int = 2
    limit_r: int = int(value_m**0.5) + 1
    while cursor_q <= limit_r:
        if value_m % cursor_q == 0:
            container_p.append(cursor_q)
            value_m //= cursor_q
            limit_r = int(value_m**0.5) + 1  # update limit as value_m changes
        else:
            cursor_q += 1
    if value_m > 1:
        container_p.append(value_m)
    return container_p