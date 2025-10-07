class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        def sortDesc(arr: list[int]) -> None:
            # Bubble sort descending as per pseudocode
            changed = True
            while changed:
                changed = False
                k = 0
                while k < len(arr) - 1:
                    if arr[k] < arr[k + 1]:
                        arr[k], arr[k + 1] = arr[k + 1], arr[k]
                        changed = True
                    k += 1

        sortDesc(horizontalCut)
        sortDesc(verticalCut)

        resultValue = 0
        idxH, idxV = 0, 0
        countH, countV = 1, 1

        while idxH < len(horizontalCut) or idxV < len(verticalCut):
            if not (idxV < len(verticalCut)) or (idxH < len(horizontalCut) and horizontalCut[idxH] > verticalCut[idxV]):
                addend = horizontalCut[idxH] * countV
                resultValue += addend
                countH += 1
                idxH += 1
            else:
                addend = verticalCut[idxV] * countH
                resultValue += addend
                countV += 1
                idxV += 1

        return resultValue