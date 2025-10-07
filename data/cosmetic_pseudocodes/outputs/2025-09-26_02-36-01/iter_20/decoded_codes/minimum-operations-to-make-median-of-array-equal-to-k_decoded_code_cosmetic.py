class Solution:
    def minOperationsToMakeMedianK(self, nums: list[int], k: int) -> int:
        def AscendSort(arr: list[int]) -> None:
            def Swap(x: int, y: int) -> None:
                arr[x], arr[y] = arr[y], arr[x]

            def Partition(low: int, high: int) -> int:
                pivotVal = arr[high]
                i = low - 1
                for j in range(low, high):
                    if arr[j] <= pivotVal:
                        i += 1
                        Swap(i, j)
                Swap(i + 1, high)
                return i + 1

            def QuickSort(low: int, high: int) -> None:
                if low < high:
                    pi = Partition(low, high)
                    QuickSort(low, pi - 1)
                    QuickSort(pi + 1, high)

            QuickSort(0, len(arr) - 1)

        AscendSort(nums)
        m = len(nums)
        p = m // 2

        def Equal(a: int, b: int) -> bool:
            return (not (a < b)) and (not (b < a))

        if Equal(nums[p], k):
            return 0

        sumOps = 0

        def Less(a: int, b: int) -> bool:
            return a < b

        def IncrementOpsForward() -> None:
            nonlocal sumOps
            q = p
            while True:
                if not Less(nums[q], k):
                    break
                delta = k - nums[q]
                sumOps += delta
                q += 1
                if q >= m:
                    break

        def IncrementOpsBackward() -> None:
            nonlocal sumOps
            r = p
            while True:
                if not Less(k, nums[r]):
                    break
                delta = nums[r] - k
                sumOps += delta
                r -= 1
                if r < 0:
                    break

        if Less(nums[p], k):
            IncrementOpsForward()
        else:
            IncrementOpsBackward()

        return sumOps