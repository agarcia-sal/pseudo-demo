from typing import List


def tri(joint_m: int) -> List[int]:
    if joint_m != 0:
        vector_z: List[int] = [1, 3]
        sentinel_x: int = 2
        while sentinel_x <= joint_m:
            if (sentinel_x % 2) == 0:
                element_y = (sentinel_x // 2) + 1
                vector_z.append(element_y)
            else:
                # indices adjusted for zero-based indexing
                element_y = vector_z[sentinel_x - 2] + vector_z[sentinel_x - 3] + ((sentinel_x + 3) // 2)
                vector_z.append(element_y)
            sentinel_x += 1
        return vector_z
    else:
        return [1]