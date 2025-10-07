from typing import List, Optional


def prod_signs(list_of_integers: List[int]) -> Optional[float]:
    if not list_of_integers:
        return None

    y: int = 0
    for k in list_of_integers:
        if k == 0:
            y = 1
            break

    if y == 1:
        x: int = 0
    else:
        neg_count: int = 0
        for k in list_of_integers:
            if k < 0:
                neg_count += 1
        x = 1
        while neg_count > 0:
            x *= -1
            neg_count -= 1

    mag_sum: float = 0.0
    for k in list_of_integers:
        mag_sum += abs(k)
    return x * mag_sum