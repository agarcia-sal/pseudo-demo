from typing import List, Dict


def common(paramA: List[str], paramB: List[str]) -> List[str]:
    accumulator: Dict[str, bool] = {}

    def helper(indexA: int) -> None:
        if indexA >= len(paramA):
            return

        indexB = 0

        def innerHelper() -> None:
            nonlocal indexB
            if indexB >= len(paramB):
                return
            if paramA[indexA] == paramB[indexB]:
                accumulator[paramA[indexA]] = True
            indexB += 1
            innerHelper()

        innerHelper()
        helper(indexA + 1)

    helper(0)
    tempList = list(accumulator.keys())
    tempList.sort()
    return tempList