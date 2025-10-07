class Solution:
    def unmarkedSumArray(self, nums, queries):
        def build_min_heap(A):
            n = len(A)

            def sift(i):
                smallest = i
                leftc = 2 * i + 1
                rightc = 2 * i + 2
                if leftc < n and A[leftc][0] < A[smallest][0]:
                    smallest = leftc
                if rightc < n and A[rightc][0] < A[smallest][0]:
                    smallest = rightc
                if smallest != i:
                    A[i], A[smallest] = A[smallest], A[i]
                    sift(smallest)

            start = (n // 2) - 1
            while start >= 0:
                sift(start)
                start -= 1

        def pop_min_heap(H):
            res = H[0]
            last_idx = len(H) - 1
            H[0] = H[last_idx]
            H.pop()
            i = 0
            size = len(H)
            while True:
                leftc = 2 * i + 1
                rightc = 2 * i + 2
                smallest = i
                if leftc < size and H[leftc][0] < H[smallest][0]:
                    smallest = leftc
                if rightc < size and H[rightc][0] < H[smallest][0]:
                    smallest = rightc
                if smallest == i:
                    break
                H[i], H[smallest] = H[smallest], H[i]
                i = smallest
            return res

        aggregator_list = [[nums[i], i] for i in range(len(nums))]
        build_min_heap(aggregator_list)

        markers_set = set()
        sum_accumulator = sum(nums)

        accumulation_result = []
        cursor_p = 0
        while cursor_p < len(queries):
            q_index, q_k = queries[cursor_p]

            if q_index not in markers_set:
                markers_set.add(q_index)
                sum_accumulator -= nums[q_index]

            subcount_c = 0
            while subcount_c < q_k and len(aggregator_list) > 0:
                val_e, idx_e = pop_min_heap(aggregator_list)
                if idx_e not in markers_set:
                    markers_set.add(idx_e)
                    sum_accumulator -= val_e
                    subcount_c += 1

            accumulation_result.append(sum_accumulator)
            cursor_p += 1

        return accumulation_result