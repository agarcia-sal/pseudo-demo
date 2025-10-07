class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        def descendingSort(arr: list[int]) -> None:
            def quicksort(low: int, high: int) -> None:
                if low >= high:
                    return
                pivot = arr[low]
                left, right = low + 1, high
                while True:
                    while left <= right and arr[left] >= pivot:
                        left += 1
                    while left <= right and arr[right] <= pivot:
                        right -= 1
                    if left > right:
                        break
                    arr[left], arr[right] = arr[right], arr[left]
                arr[low], arr[right] = arr[right], arr[low]
                quicksort(low, right - 1)
                quicksort(right + 1, high)

            quicksort(0, len(arr) - 1)

        totalCost = 0
        p = 0
        q = 0
        heightSections = 1
        widthSections = 1

        descendingSort(horizontalCut)
        descendingSort(verticalCut)

        while p < len(horizontalCut) or q < len(verticalCut):
            if q == len(verticalCut) or (p < len(horizontalCut) and horizontalCut[p] > verticalCut[q]):
                mul = widthSections
                addend = horizontalCut[p]
                heightSections += 1
                totalCost += addend * mul
                p += 1
            else:
                mul = heightSections
                addend = verticalCut[q]
                widthSections += 1
                totalCost += addend * mul
                q += 1

        return totalCost