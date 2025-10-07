from collections import defaultdict
import heapq

class Solution:
    def mostFrequentIDs(self, nums, freq):
        count = defaultdict(int)
        max_heap = []
        result = []
        for num, f in zip(nums, freq):
            count[num] += f
            heapq.heappush(max_heap, (-count[num], num))
            while max_heap and -max_heap[0][0] != count[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                result.append(-max_heap[0][0])
            else:
                result.append(0)
        return result