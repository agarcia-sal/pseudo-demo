from typing import List


def tri(integer_n: int) -> List[int]:
    return generateTri(0, integer_n, [])


def generateTri(currentIndex: int, limit: int, result: List[int]) -> List[int]:
    if not (currentIndex < limit):
        if limit == 0:
            return [1]
        return result

    if currentIndex == 0:
        result = [1, 3]
        return generateTri(currentIndex + 1, limit, result)

    if currentIndex % 2 == 0:
        newValue = (currentIndex // 2) + 1
    else:
        prev1 = result[currentIndex - 1]
        prev2 = result[currentIndex - 2]
        halfSum = (currentIndex + 3) // 2
        newValue = prev1 + prev2 + halfSum

    result.append(newValue)
    return generateTri(currentIndex + 1, limit, result)