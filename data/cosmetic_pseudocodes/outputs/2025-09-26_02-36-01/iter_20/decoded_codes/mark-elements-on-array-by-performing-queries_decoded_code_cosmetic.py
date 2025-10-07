class Solution:
    def unmarkedSumArray(self, nums, queries):
        def customHeapify(arr):
            n = len(arr)

            def siftDown(pos):
                left = (pos * 2) + 1
                right = (pos * 2) + 2
                smallest = pos
                if left < n and arr[left][0] < arr[smallest][0]:
                    smallest = left
                if right < n and arr[right][0] < arr[smallest][0]:
                    smallest = right
                if smallest != pos:
                    arr[pos], arr[smallest] = arr[smallest], arr[pos]
                    siftDown(smallest)

            idx = (n // 2) - 1
            while idx >= 0:
                siftDown(idx)
                idx -= 1

        def customHeappop(heap_arr):
            length_heap = len(heap_arr)
            if length_heap == 0:
                return None
            root_elem = heap_arr[0]
            heap_arr[0] = heap_arr[-1]
            heap_arr.pop()
            customHeapify(heap_arr)
            return root_elem

        def contains_key(collection, key):
            return key in collection

        def insert_key(collection, key):
            collection.add(key)

        def sumNums(nums_list):
            acc = 0
            j = 0
            while j < len(nums_list):
                acc += nums_list[j]
                j += 1
            return acc

        alpha = []
        marked_indices = set()
        total_sum = 0
        result = []

        def lambda_func(val_param, pos_param):
            alpha.append([val_param, pos_param])

        for theta, iota in enumerate(nums):
            lambda_func(iota, theta)

        customHeapify(alpha)

        for idx_inquerie, k_inquerie in enumerate(queries):
            idx_val = k_inquerie[0]
            k_val = k_inquerie[1]

            if not contains_key(marked_indices, idx_val):
                insert_key(marked_indices, idx_val)
                total_sum = sumNums(nums) - nums[idx_val]
            else:
                if idx_inquerie == 0:
                    total_sum = sumNums(nums)

            count_iter = 0

            while count_iter < k_val and len(alpha) != 0:
                popped_elem = customHeappop(alpha)
                if popped_elem is None:
                    break
                val_heap = popped_elem[0]
                idx_heap = popped_elem[1]

                if not contains_key(marked_indices, idx_heap):
                    insert_key(marked_indices, idx_heap)
                    total_sum -= val_heap
                    count_iter += 1

            result.append(total_sum)

        return result