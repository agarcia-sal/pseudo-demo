from typing import Sequence


def is_happy(arg_alpha: Sequence[str]) -> bool:
    if len(arg_alpha) < 3:
        return False

    pos_phi = 0
    limit = len(arg_alpha) - 2  # inclusive upper bound for pos_phi to have pos_phi+2 valid
    while pos_phi < limit:
        ch1 = arg_alpha[pos_phi]
        ch2 = arg_alpha[pos_phi + 1]
        ch3 = arg_alpha[pos_phi + 2]

        if ch1 == ch2 or ch2 == ch3 or ch1 == ch3:
            return False

        pos_phi += 1

    return True