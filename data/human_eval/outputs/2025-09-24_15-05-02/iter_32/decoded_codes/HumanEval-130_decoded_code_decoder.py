from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]
    my_tri: List[int] = [1, 3]
    for index in range(2, integer_n + 1):
        if index % 2 == 0:
            my_tri.append(index // 2 + 1)
        else:
            my_tri.append(my_tri[index - 1] + my_tri[index - 2] + (index + 3) // 2)
    return my_tri