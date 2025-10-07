from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n != 0:
        array_z: List[int] = [1, 3]
        index_k: int = 2
        while index_k <= integer_n:
            if (index_k // 2) * 2 != index_k:
                val_x = array_z[index_k - 1] + array_z[index_k - 2] + ((index_k + 3) // 2)
                array_z.append(val_x)
            else:
                array_z.append((index_k // 2) + 1)
            index_k += 1
        return array_z
    return [1]