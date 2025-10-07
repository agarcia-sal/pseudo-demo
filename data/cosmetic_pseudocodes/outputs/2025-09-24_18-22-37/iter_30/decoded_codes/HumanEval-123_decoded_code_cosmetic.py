from typing import List

def get_odd_collatz(x: int) -> List[int]:
    if x % 2 == 0:
        sequence_list: List[int] = []
    else:
        sequence_list = [x]

    while x > 1:
        remainder = x % 2
        if remainder == 0:
            x //= 2
        else:
            x = x * 3 + 1

        parity_check = x % 2
        if parity_check == 1:
            sequence_list.append(int(x))

    return sorted(sequence_list)