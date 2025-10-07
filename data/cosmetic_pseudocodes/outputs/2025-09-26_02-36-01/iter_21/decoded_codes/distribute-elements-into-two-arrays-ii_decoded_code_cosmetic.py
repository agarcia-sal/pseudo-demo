class Solution:
    def resultArray(self, nums):
        _x = 0
        _y = 1
        _a = [nums[_x]]
        _b = [nums[_y]]
        _c = [nums[_x]]
        _d = [nums[_y]]

        def binarySearchRight(arr, val):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if not (val < arr[mid]):
                    left = mid + 1
                else:
                    right = mid
            return left

        def greaterCount(arr, val):
            return len(arr) - binarySearchRight(arr, val)

        def insertIntoSorted(arr, val):
            pos = binarySearchRight(arr, val)
            arr.append(0)  # append dummy to extend size
            idx = len(arr) - 1
            while idx > pos:
                arr[idx] = arr[idx - 1]
                idx -= 1
            arr[pos] = val

        def processValue(i):
            val = nums[i]
            count1 = greaterCount(_c, val)
            count2 = greaterCount(_d, val)
            if count1 > count2:
                _a.append(val)
                insertIntoSorted(_c, val)
            elif count1 < count2:
                _b.append(val)
                insertIntoSorted(_d, val)
            else:
                if len(_a) <= len(_b):
                    _a.append(val)
                    insertIntoSorted(_c, val)
                else:
                    _b.append(val)
                    insertIntoSorted(_d, val)

        i = 2
        while i < len(nums):
            processValue(i)
            i += 1

        return _a + _b