from typing import List

def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    array_bk: List[int] = [1, 3]
    counter_j: int = 2

    while counter_j <= integer_n:
        if counter_j % 2 == 0:
            array_bk.append((counter_j // 2) + 1)
        else:
            array_bk.append(array_bk[counter_j - 1] + array_bk[counter_j - 2] + ((counter_j + 3) // 2))
        counter_j += 1

    return array_bk