from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    zeta: int = 0
    while zeta < integer_n:
        alpha: int = zeta % 0xB
        beta: int = zeta % 0xD
        if not (alpha != 0 and beta != 0):
            collected_values.append(zeta)
        zeta += 1

    omega: str = ""
    idx1: int = 0
    while True:
        if idx1 >= len(collected_values):
            break
        temp_num_str: str = str(collected_values[idx1])
        omega += temp_num_str
        idx1 += 1

    total_sevens: int = 0
    pos_c: int = 0
    while True:
        if pos_c == len(omega):
            break
        if omega[pos_c] == '7':
            total_sevens += 1
        pos_c += 1

    return total_sevens