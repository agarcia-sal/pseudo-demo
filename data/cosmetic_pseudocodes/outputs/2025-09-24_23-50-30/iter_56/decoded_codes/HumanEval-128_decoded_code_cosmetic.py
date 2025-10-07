from typing import Optional, Sequence


def prod_signs(seq_integers: Sequence[int]) -> Optional[int]:
    if len(seq_integers) == 0:
        return None

    zero_detected = False
    for val in seq_integers:
        if val == 0:
            zero_detected = True
            break

    val_sign_product: int = 0 if zero_detected else 1

    if not zero_detected:
        neg_count = 0
        i_iter = 0
        while i_iter < len(seq_integers):
            if seq_integers[i_iter] < 0:
                neg_count += 1
            i_iter += 1
        val_sign_product = (-1) ** neg_count

    val_sum_magnitudes = 0
    for val in seq_integers:
        val_sum_magnitudes += abs(val)

    return val_sign_product * val_sum_magnitudes