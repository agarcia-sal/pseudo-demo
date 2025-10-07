import heapq
from collections import defaultdict

class Solution:
    def mostFrequentIDs(self, nums, freq):
        counts = defaultdict(int)
        heap_storage = []
        output_list = []

        def upkeepHeap():
            while heap_storage and -heap_storage[0][0] != counts[heap_storage[0][1]]:
                heapq.heappop(heap_storage)

        size = len(nums)
        index1 = 0
        while index1 != size:
            current_number = nums[index1]
            increment_value = freq[index1]
            counts[current_number] += increment_value

            heap_entry = (-counts[current_number], current_number)
            heapq.heappush(heap_storage, heap_entry)

            upkeepHeap()

            if heap_storage:
                top_element = heap_storage[0]
                output_list.append(-top_element[0])
            else:
                output_list.append(0)

            index1 += 1

        return output_list