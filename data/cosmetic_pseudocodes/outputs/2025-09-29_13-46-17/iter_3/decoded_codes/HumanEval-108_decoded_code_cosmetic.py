from typing import List


def count_nums(arrayOfIntegers: List[int]) -> int:
    def digits_sum(intVal: int) -> int:
        if intVal >= 0:
            digitsList = [int(d) for d in str(intVal)]
            return sum(digitsList)
        intVal = -intVal
        signMul = -1
        digitsList = [int(d) for d in str(intVal)]
        digitsList[0] *= signMul
        return sum(digitsList)

    return len([x for x in (digits_sum(elem) for elem in arrayOfIntegers) if x > 0])