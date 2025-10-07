from typing import List


def f(nVal_integer: int) -> List[int]:
    accumulated_results: List[int] = []

    def calcProd(x_val: int, acc_prod: int) -> int:
        if x_val <= 1:
            return acc_prod
        return calcProd(x_val - 1, acc_prod * x_val)

    def calcSum(x_val: int, acc_sum: int) -> int:
        if x_val <= 0:
            return acc_sum
        return calcSum(x_val - 1, acc_sum + x_val)

    currentIndex = 1
    while currentIndex <= nVal_integer:
        if currentIndex % 2 == 0:
            factorialResult = calcProd(currentIndex, 1)
            accumulated_results.append(factorialResult)
        else:
            summationResult = calcSum(currentIndex, 0)
            accumulated_results.append(summationResult)
        currentIndex += 1

    return accumulated_results