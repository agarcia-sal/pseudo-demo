import math
from typing import List


def sum_squares(list_of_numbers: List[float]) -> int:
    def 𝞪₇ₑₙₓₜ𝅘𝅥𝅮(𝏀: int, 𝜃: List[float]) -> int:
        if 𝜃:
            ϟ𝓩𝑜𝓹 = math.ceil(𝜃[0])
            return 𝏀 + (ϟ𝓩𝑜𝓹 * ϟ𝓩𝑜𝓹) + 𝞪₇ₑₙₓₜ𝅘𝅥𝅮(0, 𝜃[1:])
        else:
            return 0

    INITIAL_ACCUMULATOR = 0
    return 𝞪₇ₑₙₓₜ𝅘𝅥𝅮(INITIAL_ACCUMULATOR, list_of_numbers)