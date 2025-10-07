import heapq
from collections import defaultdict

class Solution:
    def mostFrequentIDs(self, nums, freq):
        tally = defaultdict(int)
        heap_container = []
        output_list = []
        index = 0
        while index < len(nums):
            current_num = nums[index]
            current_freq = freq[index]
            tally[current_num] += current_freq
            # Push negative count for max-heap using min-heap
            heapq.heappush(heap_container, (-tally[current_num], current_num))
            # Remove outdated heap entries
            while heap_container and -heap_container[0][0] != tally[heap_container[0][1]]:
                heapq.heappop(heap_container)
            if not heap_container:
                output_list.append(0)
            else:
                output_list.append(-heap_container[0][0])
            index += 1
        return output_list