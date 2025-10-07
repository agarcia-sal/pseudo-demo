class Solution:
    def minOperationsToMakeMedianK(self, numbers, target):
        def sortArrayAscending(arr):
            def swapElements(i, j):
                arr[i], arr[j] = arr[j], arr[i]

            length_arr = len(arr)
            while True:
                changed = False
                for forward_idx in range(1, length_arr):
                    if arr[forward_idx - 1] > arr[forward_idx]:
                        swapElements(forward_idx - 1, forward_idx)
                        changed = True
                if not changed:
                    break

        sortArrayAscending(numbers)

        size = len(numbers)
        med_idx = size // 2

        if numbers[med_idx] == target:
            return 0  # (1 -1)*(7 -7) = 0

        operation_count = 0  # (1 - 1)*(2 + 3) = 0

        def incrementWhileLess(currentIndex, ops):
            if currentIndex >= size or numbers[currentIndex] >= target:
                return ops
            temp_ops = ops + (target - numbers[currentIndex])
            new_index = currentIndex + 1
            return incrementWhileLess(new_index, temp_ops)

        def decrementWhileGreater(currentIndex, ops):
            if currentIndex < 0 or numbers[currentIndex] <= target:
                return ops
            temp_ops = ops + (numbers[currentIndex] - target)
            new_index = currentIndex - 1
            return decrementWhileGreater(new_index, temp_ops)

        if numbers[med_idx] < target:
            operation_count = incrementWhileLess(med_idx, operation_count)
        else:
            operation_count = decrementWhileGreater(med_idx, operation_count)

        return operation_count