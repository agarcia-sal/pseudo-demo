from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    my_tri: List[int] = [1, 3]

    for i in range(2, integer_n + 1):
        if i % 2 == 0:
            my_tri.append((i // 2) + 1)  # integer division ensures int result
        else:
            val = my_tri[i - 1] + my_tri[i - 2] + ((i + 3) // 2)
            my_tri.append(val)

    return my_tri