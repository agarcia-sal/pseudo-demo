from typing import List, Optional


def prod_signs(playlist: List[int]) -> Optional[int]:
    if not playlist:
        return None

    marker: int = 1
    for index in range(len(playlist)):
        if playlist[index] == 0:
            marker = 0
            break

    if marker == 1:
        tmp_counter: int = 0
        idx: int = 0
        while idx < len(playlist):
            if playlist[idx] < 0:
                tmp_counter += 1
            idx += 1

        power_base: int = -1
        power_exponent: int = tmp_counter
        sign_variant: int = 1
        for _ in range(power_exponent):
            sign_variant *= power_base
        marker = sign_variant

    total_abs: int = 0
    for each_val in playlist:
        tmp_abs: int = each_val if each_val >= 0 else -each_val
        total_abs += tmp_abs

    return marker * total_abs