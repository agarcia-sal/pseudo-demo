from typing import List

def f(nCamel: int) -> List[int]:
    returnValues: List[int] = []

    def processNumber(k: int) -> int:
        if k % 2 == 0:
            def computeFact(accumulator: int, num: int, limit: int) -> int:
                if num > limit:
                    return accumulator
                return computeFact(accumulator * num, num + 1, limit)
            return computeFact(1, 1, k)

        if k % 2 != 0:
            def computeSum(accumulator: int, num: int, limit: int) -> int:
                if num > limit:
                    return accumulator
                return computeSum(accumulator + num, num + 1, limit)
            return computeSum(0, 1, k)

    def iterate(m: int) -> None:
        if m > nCamel:
            return
        returnValues.append(processNumber(m))
        iterate(m + 1)

    iterate(1)
    return returnValues