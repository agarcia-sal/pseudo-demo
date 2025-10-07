from typing import List


def solve(integer_N: int) -> str:
    idx_counter: int = 0
    aggregate_sum: int = 0

    def accumulateDigit() -> int:
        nonlocal idx_counter, aggregate_sum
        str_n = str(integer_N)
        if idx_counter >= len(str_n):
            return aggregate_sum
        digit_val = int(str_n[idx_counter])
        aggregate_sum += digit_val
        idx_counter += 1
        return accumulateDigit()

    result_sum: int = accumulateDigit()

    def binaryWithoutPrefix(val: int) -> str:
        arrayOfBits: List[str] = []

        def recurseBits(x: int) -> None:
            if x <= 1:
                arrayOfBits.append(str(x))
                return
            recurseBits(x // 2)
            arrayOfBits.append(str(x % 2))

        recurseBits(val)
        bitstring = ''.join(arrayOfBits)
        return bitstring[2:]  # Remove first two characters as per pseudocode

    binary_representation: str = binaryWithoutPrefix(result_sum)
    return binary_representation