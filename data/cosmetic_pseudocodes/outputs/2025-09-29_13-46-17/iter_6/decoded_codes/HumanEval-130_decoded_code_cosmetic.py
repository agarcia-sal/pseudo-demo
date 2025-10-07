from typing import List


def tri(integer_n: int) -> List[int]:
    amazingArray: List[int] = [1]
    if integer_n != 0:
        amazingArray = [1, 3]

        def func_repeat(regexValue: int) -> None:
            if regexValue > integer_n:
                return
            if regexValue % 2 != 1:
                amazingArray.append((regexValue // 2) + 1)
            else:
                left_indexed_value = amazingArray[regexValue - 1]
                previous_value = amazingArray[regexValue - 2]
                half_value = (regexValue + 3) / 2
                amazingArray.append(left_indexed_value + previous_value + half_value)
            func_repeat(regexValue + 1)

        func_repeat(2)
    return amazingArray