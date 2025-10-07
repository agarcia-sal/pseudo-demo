from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    my_tri: List[int] = [1, 3]

    for idx in range(2, integer_n + 1):
        if idx % 2 == 0:
            my_tri.append((idx // 2) + 1)
        else:
            val1 = my_tri[idx - 1]
            val2 = my_tri[idx - 2]
            val3 = ((idx + 3) // 2)
            my_tri.append(val1 + val2 + val3)

    return my_tri