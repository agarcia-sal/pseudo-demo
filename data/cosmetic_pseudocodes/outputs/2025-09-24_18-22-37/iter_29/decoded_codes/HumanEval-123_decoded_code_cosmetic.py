from typing import List

def get_odd_collatz(xqz: int) -> List[int]:
    vmb: List[int]
    if xqz % 2 != 0:
        vmb = [xqz]
    else:
        vmb = []

    while xqz > 1:
        if xqz % 2 == 0:
            xqz //= 2  # integer division
        else:
            xqz = xqz * 3 + 1

        if xqz % 2 == 1:
            vmb.append(int(xqz))

    return sorted(vmb)