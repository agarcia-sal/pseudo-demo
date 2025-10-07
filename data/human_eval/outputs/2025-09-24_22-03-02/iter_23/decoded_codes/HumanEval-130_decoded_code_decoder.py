from typing import List

def tri(n: int) -> List[int]:
    if n == 0:
        return [1]
    my_tri = [1, 3]
    i = 2
    while i <= n:
        if i % 2 == 0:
            my_tri.append(i // 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) // 2)
        i += 1
    return my_tri