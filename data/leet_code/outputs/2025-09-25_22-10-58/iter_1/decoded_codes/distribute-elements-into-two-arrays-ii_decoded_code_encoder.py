from bisect import bisect_right, insort

class Solution:
    def resultArray(self, nums):
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        sorted_arr1 = [nums[0]]
        sorted_arr2 = [nums[1]]

        def greaterCount(arr, val):
            pos = bisect_right(arr, val)
            return len(arr) - pos

        for val in nums[2:]:
            count1 = greaterCount(sorted_arr1, val)
            count2 = greaterCount(sorted_arr2, val)

            if count1 > count2:
                arr1.append(val)
                insort(sorted_arr1, val)
            elif count1 < count2:
                arr2.append(val)
                insort(sorted_arr2, val)
            else:
                if len(arr1) <= len(arr2):
                    arr1.append(val)
                    insort(sorted_arr1, val)
                else:
                    arr2.append(val)
                    insort(sorted_arr2, val)

        return arr1 + arr2