from typing import Union

def circular_shift(value_m: Union[int, str], amount_n: int) -> str:
    sequence_p: str = str(value_m)
    length_q: int = len(sequence_p)
    if not(amount_n <= length_q):
        return sequence_p[::-1]
    else:
        pivot_r: int = length_q - amount_n
        return sequence_p[pivot_r:] + sequence_p[:pivot_r]