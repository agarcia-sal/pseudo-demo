class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        def descendSort(arr: list[int]) -> None:
            idx = len(arr) - 1
            while True:
                swapped = False
                k = 0
                while k < idx:
                    if arr[k] < arr[k + 1]:
                        arr[k], arr[k + 1] = arr[k + 1], arr[k]
                        swapped = True
                    k += 1
                idx -= 1
                if not swapped:
                    break

        descendSort(horizontalCut)
        descendSort(verticalCut)

        result = 0
        alpha = 0
        beta = 0
        gamma = 1
        delta = 1

        def repeatCondition() -> bool:
            return alpha < m - 1 or beta < n - 1

        while repeatCondition():
            condFirst = beta == n - 1
            condSecond = alpha < m - 1
            condThird = horizontalCut[alpha] > verticalCut[beta]
            combinedCond = condFirst or (condSecond and condThird)
            if combinedCond:
                tempCalc = horizontalCut[alpha] * delta
                result += tempCalc
                gamma += 1
                alpha += 1
            else:
                tempCalc2 = verticalCut[beta] * gamma
                result += tempCalc2
                delta += 1
                beta += 1

        return result