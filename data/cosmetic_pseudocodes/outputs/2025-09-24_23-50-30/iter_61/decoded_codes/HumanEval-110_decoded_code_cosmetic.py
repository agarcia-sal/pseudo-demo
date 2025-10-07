from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    def loopOne(aList: List[int], idx: int, c_odd: int) -> int:
        if idx < len(aList):
            if (aList[idx] % 2) == 1:
                return loopOne(aList, idx + 1, c_odd + 1)
            else:
                return loopOne(aList, idx + 1, c_odd)
        return c_odd

    def loopTwo(bList: List[int], jdx: int, c_even: int) -> int:
        if jdx >= len(bList):
            return c_even
        if (bList[jdx] % 2) == 0:
            return loopTwo(bList, jdx + 1, c_even + 1)
        return loopTwo(bList, jdx + 1, c_even)

    odd_counter = loopOne(list_one, 0, 0)
    even_counter = loopTwo(list_two, 0, 0)

    return "YES" if even_counter >= odd_counter else "NO"