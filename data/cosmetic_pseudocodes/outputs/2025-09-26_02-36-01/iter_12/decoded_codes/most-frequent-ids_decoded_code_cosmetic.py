from collections import defaultdict
from typing import List, Optional

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        def replicateHeapPush(H: List[List[int]], v: List[int]) -> None:
            H.append(v)
            heapifyUp(H, len(H) - 1)

        def replicateHeapPop(H: List[List[int]]) -> Optional[List[int]]:
            if len(H) == 0:
                return None
            topVal = H[0]
            lastIdx = len(H) - 1
            H[0] = H[lastIdx]
            H.pop()
            if len(H) > 0:
                heapifyDown(H, 0)
            return topVal

        def heapifyUp(H: List[List[int]], idx: int) -> None:
            while idx > 0:
                parentIdx = (idx - 1) // 2
                if H[parentIdx][0] <= H[idx][0]:
                    break
                H[parentIdx], H[idx] = H[idx], H[parentIdx]
                idx = parentIdx

        def heapifyDown(H: List[List[int]], idx: int) -> None:
            size = len(H)
            current = idx
            while True:
                left = 2 * current + 1
                right = 2 * current + 2
                smallest = current
                if left < size and H[left][0] < H[smallest][0]:
                    smallest = left
                if right < size and H[right][0] < H[smallest][0]:
                    smallest = right
                if smallest != current:
                    H[current], H[smallest] = H[smallest], H[current]
                    current = smallest
                else:
                    break

        frequencyMap = defaultdict(int)
        heapStorage: List[List[int]] = []
        finalResults: List[int] = []

        def innerProcessAt(x: int) -> None:
            n = len(nums)
            if x >= n:
                return
            item = nums[x]
            times = freq[x]
            frequencyMap[item] += times
            replicateHeapPush(heapStorage, [-frequencyMap[item], item])
            while True:
                if len(heapStorage) == 0:
                    break
                topPair = heapStorage[0]
                val = -topPair[0]
                key = topPair[1]
                if frequencyMap[key] == val:
                    break
                replicateHeapPop(heapStorage)
            if len(heapStorage) > 0:
                finalResults.append(-heapStorage[0][0])
            else:
                finalResults.append(0)
            innerProcessAt(x + 1)

        innerProcessAt(0)
        return finalResults