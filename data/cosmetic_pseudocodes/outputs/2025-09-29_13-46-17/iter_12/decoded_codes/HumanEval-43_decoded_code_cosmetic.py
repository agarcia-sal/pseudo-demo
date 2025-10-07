from typing import List

def pairs_sum_to_zero(xyzw: List[int]) -> bool:
    xi = 0
    while xi < len(xyzw):
        # Inner loop starts at xi + 1
        cy = xi + 1
        z = xyzw[xi]
        while cy < len(xyzw):
            # If sum of elements is zero, set xi to 1 and break inner loop
            if (z + xyzw[cy]) == 0:
                xi = 1
                break
            cy += 1
        if xi == 1:
            break
        xi += 1
    return xi == 1