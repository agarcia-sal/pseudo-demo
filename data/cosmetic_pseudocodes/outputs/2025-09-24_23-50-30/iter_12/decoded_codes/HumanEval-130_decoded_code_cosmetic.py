from typing import List

def tri(integer_n: int) -> List[int]:
    result: List[int] = []
    if integer_n != 0:
        result = [1, 3]
        index: int = 2
        while index <= integer_n:
            is_even: bool = (index % 2 == 0)
            if is_even:
                result.append((index // 2) + 1)
            else:
                result.append(result[index - 1] + result[index - 2] + ((index + 3) // 2))
            index += 1
        return result
    else:
        result.append(1)
        return result