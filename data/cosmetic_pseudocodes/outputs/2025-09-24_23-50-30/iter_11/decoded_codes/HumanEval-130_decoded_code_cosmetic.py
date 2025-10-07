from typing import List

def tri(p_val: int) -> List[int]:
    if p_val == 0:
        return [1]

    kst: List[int] = [1, 3]
    cv = 2
    while cv <= p_val:
        if cv % 2 == 0:
            kst.append(cv // 2 + 1)  # integer division
        else:
            kst.append(kst[cv - 1] + kst[cv - 2] + ((cv + 3) // 2))
        cv += 1

    return kst