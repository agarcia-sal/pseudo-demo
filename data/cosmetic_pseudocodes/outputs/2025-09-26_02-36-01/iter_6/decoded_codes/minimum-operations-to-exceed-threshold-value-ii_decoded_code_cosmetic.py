class Solution:
    def minOperations(self, nums, k):
        def ExtractMinHeap(heap):
            if len(heap) == 0:
                return None
            first_element = heap[0]
            last_element_index = len(heap) - 1
            heap[0] = heap[last_element_index]
            heap.pop()
            SiftDown(0, heap)
            return first_element

        def SiftDown(index, heap):
            heap_size = len(heap)

            def LeftChild(i):
                return 2 * i + 1

            def RightChild(i):
                return 2 * i + 2

            current = index
            while True:
                left_idx = LeftChild(current)
                right_idx = RightChild(current)
                smallest = current

                if left_idx < heap_size and heap[left_idx] < heap[smallest]:
                    smallest = left_idx
                if right_idx < heap_size and heap[right_idx] < heap[smallest]:
                    smallest = right_idx

                if smallest == current:
                    break

                heap[current], heap[smallest] = heap[smallest], heap[current]
                current = smallest

        def SiftUp(index, heap):
            def Parent(i):
                return (i - 1) // 2

            current = index
            while current > 0:
                parent_idx = Parent(current)
                if heap[parent_idx] <= heap[current]:
                    break
                heap[parent_idx], heap[current] = heap[current], heap[parent_idx]
                current = parent_idx

        def Heapify(array):
            count = len(array)
            start_index = (count // 2) - 1
            for idx in range(start_index, -1, -1):
                SiftDown(idx, array)

        def PushHeap(heap, value):
            heap.append(value)
            SiftUp(len(heap) - 1, heap)

        def ConditionCheck(arr, limit):
            return not (arr[0] >= limit or len(arr) <= 1)

        def Combine(a, b):
            return (a + a) + b

        Heapify(nums)
        total_operations = 0

        while ConditionCheck(nums, k):
            first_min = ExtractMinHeap(nums)
            second_min = ExtractMinHeap(nums)
            combined_value = Combine(first_min, second_min)
            PushHeap(nums, combined_value)
            total_operations += 1

        return total_operations