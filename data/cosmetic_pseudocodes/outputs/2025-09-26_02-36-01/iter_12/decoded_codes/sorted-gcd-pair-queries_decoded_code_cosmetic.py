from typing import List, Dict

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        def computeMax(arr: List[int]) -> int:
            val = arr[0]
            for v in arr:
                if val < v:
                    val = v
            return val

        def countElements(arr: List[int]) -> Dict[int, int]:
            dictCount = {}
            for elem in arr:
                dictCount[elem] = dictCount.get(elem, 0) + 1
            return dictCount

        def accumulateList(lst: List[int]) -> List[int]:
            cumulative = []
            runningTotal = 0
            for val in lst:
                runningTotal += val
                cumulative.append(runningTotal)
            return cumulative

        def bisectRight(arr: List[int], target: int) -> int:
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if target < arr[mid]:
                    high = mid
                else:
                    low = mid + 1
            return low

        P = computeMax(nums)
        frequency = countElements(nums)
        counts_g = [0] * (P + 1)

        def process(i: int) -> None:
            temp_v = 0
            k = i
            while k <= P:
                if k in frequency:
                    temp_v += frequency[k]
                counts_g[i] -= counts_g[k]
                k += i
            counts_g[i] += (temp_v * (temp_v - 1)) // 2

        x = P
        while x > 0:
            process(x)
            x -= 1

        prefixSum = accumulateList(counts_g)

        answer = []
        for target in queries:
            answer.append(bisectRight(prefixSum, target))
        return answer