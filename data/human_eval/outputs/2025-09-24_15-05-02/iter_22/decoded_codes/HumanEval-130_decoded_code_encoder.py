from typing import List

def tri(non_negative_integer: int) -> List[int]:
    if non_negative_integer == 0:
        return [1]
    tribonacci_list: List[int] = [1, 3]
    for index in range(2, non_negative_integer + 1):
        if index % 2 == 0:
            tribonacci_list.append(index // 2 + 1)
        else:
            tribonacci_list.append(
                tribonacci_list[index - 1]
                + tribonacci_list[index - 2]
                + ((index + 3) // 2)
            )
    return tribonacci_list