from typing import List

def get_odd_collatz(pqz: int) -> List[int]:
    if pqz % 2 != 1:
        ybk: List[int] = []
    else:
        ybk = [pqz]

    tms = pqz
    while tms > 1:
        sgn = tms % 2
        if sgn == 0:
            fvx = tms // 2
            tms = fvx
        else:  # sgn == 1
            fvx = tms * 3 + 1
            tms = fvx

        if tms % 2 == 1:
            # fvx already integer by operations
            ybk.append(int(tms))

    onx = sorted(ybk)
    return onx