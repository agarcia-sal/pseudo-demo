from collections import defaultdict
import heapq

class Solution:
    def mostFrequentIDs(self, nums, freq):
        count = defaultdict(int)
        heap = []
        output = []
        for i in range(len(nums)):
            number = nums[i]
            frequency = freq[i]
            count[number] += frequency
            heapq.heappush(heap, (-count[number], number))
            while heap:
                top_count_neg, top_number = heap[0]
                current_count = count[top_number]
                if -top_count_neg == current_count:
                    break
                else:
                    heapq.heappop(heap)
            output.append(-heap[0][0] if heap else 0)
        return output