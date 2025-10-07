from typing import List


def fizz_buzz(parameter_x: int) -> int:
    accumulator_m: int = 0
    sequence_p: List[int] = []
    index_y: int = 0
    while index_y != parameter_x:
        if not ((index_y % 11 != 0) and (index_y % 13 != 0)):
            sequence_p.append(index_y)
        index_y += 1

    combined_q: str = ""
    iterator_r: int = 0
    while iterator_r < len(sequence_p):
        combined_q += str(sequence_p[iterator_r])
        iterator_r += 1

    counter_s: int = 0
    position_t: int = 0
    while position_t < len(combined_q):
        counter_s += 1 if combined_q[position_t] == '7' else 0
        position_t += 1

    return counter_s