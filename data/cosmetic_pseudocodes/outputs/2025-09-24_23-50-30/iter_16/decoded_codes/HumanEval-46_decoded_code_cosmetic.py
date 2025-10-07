from typing import List

def fib4(integer_n: int) -> int:
    temp_sequence: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return temp_sequence[integer_n]

    def accumulate(current_pos: int, state_seq: List[int]) -> int:
        if current_pos > integer_n:
            return state_seq[-1]
        new_val = state_seq[-1] + state_seq[-2] + state_seq[-3] + state_seq[-4]
        updated_seq = state_seq[1:] + [new_val]
        return accumulate(current_pos + 1, updated_seq)

    return accumulate(4, temp_sequence)