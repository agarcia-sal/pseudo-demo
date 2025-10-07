class Solution:
    def minOperations(self, nums, k):
        m = len(nums)

        def sift_down(arr, start, end_):
            root = start
            while True:
                child = 2 * root + 1
                if child >= end_:
                    break
                if child + 1 < end_ and arr[child + 1] < arr[child]:
                    child += 1
                if arr[root] <= arr[child]:
                    break
                else:
                    arr[root], arr[child] = arr[child], arr[root]
                    root = child

        def heapify_local(arr):
            n = len(arr)
            i = n // 2 - 1
            while i >= 0:
                sift_down(arr, i, n)
                i -= 1

        def heappop_local(heap):
            if len(heap) == 0:
                return None
            last_elem = heap[-1]
            result = heap[0]
            heap[0] = last_elem
            heap.pop()
            if heap:
                sift_down(heap, 0, len(heap))
            return result

        def heappush_local(heap, val):
            heap.append(val)
            idx = len(heap) - 1
            while idx > 0:
                parent_idx = (idx - 1) // 2
                if heap[parent_idx] > heap[idx]:
                    heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
                    idx = parent_idx
                else:
                    break

        heapify_local(nums)
        count_operations = 0

        while True:
            if len(nums) <= 1:
                break
            if not (nums[0] < k):
                break
            first_min = heappop_local(nums)
            second_min = heappop_local(nums)
            val_one, val_two = first_min, second_min
            if val_one > val_two:
                val_one, val_two = val_two, val_one
            computed_val = val_one * 2 + val_two
            heappush_local(nums, computed_val)
            count_operations += 1

        return count_operations