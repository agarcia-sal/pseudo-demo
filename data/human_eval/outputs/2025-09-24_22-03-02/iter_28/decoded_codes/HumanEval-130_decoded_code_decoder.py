from typing import List

def tri(n: int) -> List[int]:
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            value = 1 + i // 2
            my_tri.append(value)
        else:
            value = my_tri[i - 1] + my_tri[i - 2] + (i + 3) // 2
            my_tri.append(value)
    return my_tri