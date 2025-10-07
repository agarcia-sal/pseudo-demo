class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:

        def sortDesc(arr: list[int], lengthVal: int) -> None:
            if lengthVal <= 1:
                return
            pivotIndex = lengthVal - 1
            leftSide = 0
            rightSide = pivotIndex - 1
            while leftSide <= rightSide:
                while leftSide < lengthVal and arr[leftSide] > arr[pivotIndex]:
                    leftSide += 1
                while rightSide >= 0 and arr[rightSide] <= arr[pivotIndex]:
                    rightSide -= 1
                if leftSide < rightSide:
                    arr[leftSide], arr[rightSide] = arr[rightSide], arr[leftSide]
                    leftSide += 1
                    rightSide -= 1
            arr[leftSide], arr[pivotIndex] = arr[pivotIndex], arr[leftSide]
            sortDesc(arr, leftSide)
            sortDesc(arr[leftSide + 1:], lengthVal - leftSide - 1)
            # Note: above recursion with arr[leftSide + 1:] creates a new list slice,
            # but original algorithm expects in-place. Instead, we adjust to sort in place.

        # To fix in-place sorting on right side:
        # Redefine sortDesc to accept start and end indexes.
        def sortDescInPlace(arr: list[int], start: int, end: int) -> None:
            if end - start + 1 <= 1:
                return
            pivotIndex = end
            leftSide = start
            rightSide = end - 1
            while leftSide <= rightSide:
                while leftSide <= end and arr[leftSide] > arr[pivotIndex]:
                    leftSide += 1
                while rightSide >= start and arr[rightSide] <= arr[pivotIndex]:
                    rightSide -= 1
                if leftSide < rightSide:
                    arr[leftSide], arr[rightSide] = arr[rightSide], arr[leftSide]
                    leftSide += 1
                    rightSide -= 1
            arr[leftSide], arr[pivotIndex] = arr[pivotIndex], arr[leftSide]
            sortDescInPlace(arr, start, leftSide - 1)
            sortDescInPlace(arr, leftSide + 1, end)

        sortDescInPlace(horizontalCut, 0, len(horizontalCut) - 1)
        sortDescInPlace(verticalCut, 0, len(verticalCut) - 1)

        indexH = 0
        indexV = 0
        heightCount = 1
        widthCount = 1

        def processCuts(posH: int, posV: int, accCost: int, heightSeg: int, widthSeg: int) -> int:
            if posH >= len(horizontalCut) and posV >= len(verticalCut):
                return accCost
            if (posV >= len(verticalCut)) or (
                posH < len(horizontalCut) and horizontalCut[posH] > verticalCut[posV]
            ):
                updatedCost = accCost + horizontalCut[posH] * widthSeg
                return processCuts(posH + 1, posV, updatedCost, heightSeg + 1, widthSeg)
            else:
                updatedCost = accCost + verticalCut[posV] * heightSeg
                return processCuts(posH, posV + 1, updatedCost, heightSeg, widthSeg + 1)

        accumulatedCost = processCuts(indexH, indexV, 0, heightCount, widthCount)
        return accumulatedCost