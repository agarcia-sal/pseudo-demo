class Solution:
    def resultArray(self, nums):
        left_list = [nums[0]]
        right_list = [nums[1]]
        left_sorted = [nums[0]]
        right_sorted = [nums[1]]

        def countGreater(sequence, reference):
            def binarySearchRight(seq, key, low, high):
                if low == high:
                    return low
                mid = low + (high - low) // 2
                if seq[mid] <= key:
                    return binarySearchRight(seq, key, mid + 1, high)
                else:
                    return binarySearchRight(seq, key, low, mid)
            insertionIndex = binarySearchRight(sequence, reference, 0, len(sequence))
            totalElements = len(sequence)
            return totalElements - insertionIndex

        def insertSorted(arr, elem):
            def binarySearchLeft(arrb, keyb, lowb, highb):
                if lowb == highb:
                    return lowb
                midb = lowb + (highb - lowb) // 2
                if arrb[midb] >= keyb:
                    return binarySearchLeft(arrb, keyb, lowb, midb)
                else:
                    return binarySearchLeft(arrb, keyb, midb + 1, highb)
            pos_to_insert = binarySearchLeft(arr, elem, 0, len(arr))
            # slicing handles boundaries correctly
            first_part = arr[:pos_to_insert]
            second_part = arr[pos_to_insert:]
            return first_part + [elem] + second_part

        def processIndex(current):
            if current > (len(nums) - 1):
                return
            current_value = nums[current]
            left_count = countGreater(left_sorted, current_value)
            right_count = countGreater(right_sorted, current_value)

            nonlocal left_list, right_list, left_sorted, right_sorted

            if left_count > right_count:
                left_list = left_list + [current_value]
                left_sorted = insertSorted(left_sorted, current_value)
            elif left_count < right_count:
                right_list = right_list + [current_value]
                right_sorted = insertSorted(right_sorted, current_value)
            else:
                if len(left_list) <= len(right_list):
                    left_list = left_list + [current_value]
                    left_sorted = insertSorted(left_sorted, current_value)
                else:
                    right_list = right_list + [current_value]
                    right_sorted = insertSorted(right_sorted, current_value)
            processIndex(current + 1)

        processIndex(2)
        combined_result = left_list + right_list
        return combined_result