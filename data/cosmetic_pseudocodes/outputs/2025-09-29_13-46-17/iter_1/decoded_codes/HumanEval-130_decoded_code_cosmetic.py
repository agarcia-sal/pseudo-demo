from typing import List

def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    my_tri: List[int] = [1, 3]

    for integer_i in range(2, integer_n + 1):
        if integer_i % 2 == 0:
            my_tri.append(integer_i // 2 + 1)
        else:
            my_tri.append(my_tri[integer_i - 1] + my_tri[integer_i - 2] + ((integer_i + 3) // 2))

    return my_tri