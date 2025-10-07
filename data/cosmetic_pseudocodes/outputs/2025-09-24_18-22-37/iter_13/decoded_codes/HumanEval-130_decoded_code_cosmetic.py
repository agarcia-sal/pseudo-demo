from typing import List

def tri(xr: int) -> List[int]:
    ab: List[int] = [1]
    if xr != 0:
        cd: List[int] = [1, 3]
        ef: int = 2
        while ef <= xr:
            gh: int = ef % 2
            if gh == 0:
                ij: int = ef // 2 + 1
                cd.append(ij)
            else:
                kl: int = cd[ef - 1] + cd[ef - 2]
                mn: int = (ef + 3) // 2
                op: int = kl + mn
                cd.append(op)
            ef += 1
        ab = cd
    return ab