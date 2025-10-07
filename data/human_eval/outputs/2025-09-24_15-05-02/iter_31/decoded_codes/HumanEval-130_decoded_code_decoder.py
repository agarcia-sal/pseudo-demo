from typing import List


def tri(non_negative_integer_n: int) -> List[int]:
    if non_negative_integer_n == 0:
        return [1]
    my_tribonacci_list = [1, 3]
    for index in range(2, non_negative_integer_n + 1):
        if index % 2 == 0:
            my_tribonacci_list.append(index // 2 + 1)
        else:
            my_tribonacci_list.append(
                my_tribonacci_list[index - 1]
                + my_tribonacci_list[index - 2]
                + (index + 3) // 2
            )
    return my_tribonacci_list