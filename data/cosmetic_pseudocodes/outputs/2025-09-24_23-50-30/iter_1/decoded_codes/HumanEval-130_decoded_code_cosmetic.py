from typing import List

def tri(integer_n: int) -> List[int]:
    my_tri: List[int] = []
    if integer_n == 0:
        my_tri.append(1)
        return my_tri

    my_tri.extend([1, 3])

    integer_i: int = 2
    while integer_i <= integer_n:
        if (integer_i % 2) == 0:
            my_tri.append(int(integer_i / 2 + 1))
        else:
            my_tri.append(
                my_tri[integer_i - 1] + my_tri[integer_i - 2] + int((integer_i + 3) / 2)
            )
        integer_i += 1

    return my_tri