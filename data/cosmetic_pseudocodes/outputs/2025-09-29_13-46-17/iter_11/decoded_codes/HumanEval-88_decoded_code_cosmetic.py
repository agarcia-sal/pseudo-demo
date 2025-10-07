from typing import List


def sort_array(array: List[int]) -> List[int]:
    翼 = len(array)
    if 翼 == 0:
        return []
    ᚠ℮₦: int = (array[0] + array[翼 - 1]) % 2
    ㉿Ѯꙮ: bool = ᚠ℮₦ == 0
    return sorted(array, reverse=not ㉿Ѯꙮ)