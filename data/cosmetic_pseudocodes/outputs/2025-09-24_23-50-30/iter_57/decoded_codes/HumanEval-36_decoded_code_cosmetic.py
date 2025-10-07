from typing import List


def fizz_buzz(magnitude_p: int) -> int:
    accumulator_Q: List[int] = []
    pointer_U: int = 0

    while pointer_U < magnitude_p:
        # Append pointer_U if it is divisible by 11 or 13
        if not (pointer_U % 11 != 0 and pointer_U % 13 != 0):
            accumulator_Q.append(pointer_U)
        pointer_U += 1

    builder_R: str = ""
    iterator_Z: int = 0

    while iterator_Z < len(accumulator_Q):
        builder_R += str(accumulator_Q[iterator_Z])
        iterator_Z += 1

    tally_D: int = 0
    index_S: int = 0

    while index_S < len(builder_R):
        if builder_R[index_S] == "7":
            tally_D += 1
        index_S += 1

    return tally_D