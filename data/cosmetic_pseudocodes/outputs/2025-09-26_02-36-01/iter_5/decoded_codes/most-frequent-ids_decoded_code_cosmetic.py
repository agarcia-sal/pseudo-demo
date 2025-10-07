from collections import defaultdict
import heapq

class Solution:
    def mostFrequentIDs(self, nums, freq):
        frequency_map = defaultdict(int)
        heap_storage = []
        output_list = []

        def prune_heap():
            # Remove heap top elements if freq does not match current frequency_map
            while heap_storage and frequency_map[heap_storage[0][1]] != -heap_storage[0][0]:
                heapq.heappop(heap_storage)

        def process_index(index):
            if index == len(nums):
                return

            current_num = nums[index]
            current_freq = freq[index]
            frequency_map[current_num] += current_freq

            neg_count = -frequency_map[current_num]
            heapq.heappush(heap_storage, (neg_count, current_num))

            prune_heap()

            if heap_storage:
                top_val = -heap_storage[0][0]
                output_list.append(top_val)
            else:
                output_list.append(0)

            process_index(index + 1)

        process_index(0)
        return output_list