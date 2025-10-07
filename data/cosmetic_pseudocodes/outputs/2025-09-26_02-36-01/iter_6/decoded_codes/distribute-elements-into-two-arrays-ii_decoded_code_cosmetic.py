class Solution:
    def resultArray(self, nums):
        init_a = [nums[0]]
        init_b = [nums[1]]
        ordered_a = [nums[0]]
        ordered_b = [nums[1]]

        def countGreater(arrx, valu):
            def binSearchRight(arr, v, low, high):
                if low >= high:
                    return low
                med = low + (high - low) // 2
                if not (arr[med] <= v):
                    return binSearchRight(arr, v, low, med)
                else:
                    return binSearchRight(arr, v, med + 1, high)

            posx = binSearchRight(arrx, valu, 0, len(arrx))
            return len(arrx) - posx

        def insertSorted(arr_sort, value, start, endd):
            if start < endd:
                midp = start + (endd - start) // 2
                if arr_sort[midp] < value:
                    insertSorted(arr_sort, value, midp + 1, endd)
                else:
                    insertSorted(arr_sort, value, start, midp)
            else:
                arr_sort.insert(start, value)

        def loopIndex(j):
            if j > len(nums) - 1:
                return
            valx = nums[j]

            count_a = countGreater(ordered_a, valx)
            count_b = countGreater(ordered_b, valx)

            if count_a > count_b:
                init_a.append(valx)
                insertSorted(ordered_a, valx, 0, len(ordered_a))
            elif count_a < count_b:
                init_b.append(valx)
                insertSorted(ordered_b, valx, 0, len(ordered_b))
            else:
                if len(init_a) <= len(init_b):
                    init_a.append(valx)
                    insertSorted(ordered_a, valx, 0, len(ordered_a))
                else:
                    init_b.append(valx)
                    insertSorted(ordered_b, valx, 0, len(ordered_b))

            loopIndex(j + 1)

        loopIndex(2)

        resultlist = []
        for k in range(len(init_a)):
            resultlist.append(init_a[k])
        for k in range(len(init_b)):
            resultlist.append(init_b[k])

        return resultlist