from typing import List


def fib4(integer_p: int) -> int:
    result_sequence: List[int] = [0, 0, 2, 0]
    if integer_p < 4:
        return result_sequence[integer_p]

    idx_counter = 4
    while idx_counter <= integer_p:
        val_a = result_sequence[3]
        val_b = result_sequence[2]
        val_c = result_sequence[1]
        val_d = result_sequence[0]
        next_val = val_a + val_b + val_c + val_d

        result_sequence.append(next_val)
        result_sequence.pop(0)

        idx_counter += 1

    return result_sequence[3]