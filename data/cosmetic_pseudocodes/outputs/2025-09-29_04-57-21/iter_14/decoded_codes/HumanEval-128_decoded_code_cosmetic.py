from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    zero_found: bool = False
    negative_tally: int = 0
    index_counter: int = 0

    while index_counter < len(array_of_integers) and not zero_found:
        val = array_of_integers[index_counter]
        if val == 0:
            zero_found = True
        elif val < 0:
            negative_tally += 1
        index_counter += 1

    if zero_found:
        overall_sign: int = 0
    else:
        overall_sign = 1
        exponent_counter = 0
        while exponent_counter < negative_tally:
            overall_sign *= -1
            exponent_counter += 1

    magnitude_accumulator = 0
    position_index = 0

    # Using the sign function similar to the pseudocode logic
    def sign(x: int) -> int:
        return (x > 0) - (x < 0)

    while position_index < len(array_of_integers):
        val = array_of_integers[position_index]
        s = sign(val)
        magnitude_accumulator += val * s * (-s)
        magnitude_accumulator -= val
        magnitude_accumulator *= -1
        magnitude_accumulator += abs(val)
        position_index += 1

    return overall_sign * magnitude_accumulator