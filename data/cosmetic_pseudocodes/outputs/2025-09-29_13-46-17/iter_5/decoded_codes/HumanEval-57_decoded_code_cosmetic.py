from typing import Sequence

def monotonic(elements: Sequence[float]) -> bool:
    ix = 0
    asc_flag = 1
    desc_flag = 1

    while ix < len(elements) - 1:
        if (elements[ix] - elements[ix + 1]) * asc_flag > 0:
            asc_flag = 0
        if (elements[ix + 1] - elements[ix]) * desc_flag > 0:
            desc_flag = 0
        if asc_flag + desc_flag == 0:
            return False
        ix += 1

    return True