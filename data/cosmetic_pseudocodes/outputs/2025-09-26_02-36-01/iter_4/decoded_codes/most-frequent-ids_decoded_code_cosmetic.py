import heapq
from collections import defaultdict

class Solution:
    def mostFrequentIDs(self, nums, freq):
        freq_map = defaultdict(int)
        heap_container = []
        output_list = []
        for i in range(len(nums)):
            current_num = nums[i]
            current_freq = freq[i]
            freq_map[current_num] += current_freq
            neg_freq = -freq_map[current_num]
            heapq.heappush(heap_container, (neg_freq, current_num))
            # Remove outdated heap entries
            while heap_container and -heap_container[0][0] != freq_map[heap_container[0][1]]:
                heapq.heappop(heap_container)
            if heap_container:
                output_list.append(-heap_container[0][0])
            else:
                output_list.append(0)
        return output_list