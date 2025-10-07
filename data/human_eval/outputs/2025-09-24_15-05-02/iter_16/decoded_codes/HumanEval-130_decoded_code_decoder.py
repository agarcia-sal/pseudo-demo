from typing import List

def tri(n: int) -> List[int]:
    if n == 0:
        return [1]

    my_tribonacci_list: List[int] = [1, 3]

    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tribonacci_list.append(1 + i // 2)
        else:
            my_tribonacci_list.append(
                my_tribonacci_list[i - 1] + my_tribonacci_list[i - 2] + ((i + 3) // 2)
            )

    return my_tribonacci_list