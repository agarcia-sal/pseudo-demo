from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]
    result: List[int] = [1, 3]
    index = 2
    while index <= integer_n:
        is_even = (index % 2 == 0)
        if is_even:
            val = (index // 2) + 1
            result.append(val)
        else:
            val = result[index - 1] + result[index - 2] + ((index + 3) // 2)
            result.append(val)
        index += 1
    return result