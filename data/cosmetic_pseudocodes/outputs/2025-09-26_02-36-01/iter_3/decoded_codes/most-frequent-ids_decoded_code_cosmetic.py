from collections import defaultdict
import heapq

class Solution:
    def mostFrequentIDs(self, nums, freq):
        tally = defaultdict(int)
        heap_container = []
        output = []
        idx = 0
        while idx < len(nums):
            element = nums[idx]
            increment = freq[idx]
            tally[element] += increment
            heapq.heappush(heap_container, (-tally[element], element))
            # Remove outdated entries
            while heap_container and -heap_container[0][0] != tally[heap_container[0][1]]:
                heapq.heappop(heap_container)
            if heap_container:
                current_max = -heap_container[0][0]
                output.append(current_max)
            else:
                output.append(0)
            idx += 1
        return output