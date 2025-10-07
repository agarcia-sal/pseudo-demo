from bisect import insort

class Solution:
    def resultArray(self, nums):
        pqr = [nums[0]]
        xyz = [nums[1]]
        abc = [nums[0]]
        def_ = [nums[1]]

        def binarySearchRight(arr, key, start, end):
            while start < end:
                mid = (start + end) // 2
                if arr[mid] <= key:
                    start = mid + 1
                else:
                    end = mid
            if start < len(arr) and arr[start] <= key:
                return start + 1
            return start

        def helper(mno, uvw):
            pos = binarySearchRight(mno, uvw, 0, len(mno) - 1)
            return len(mno) - pos

        def insertSorted(arr, val):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            arr.insert(left, val)

        def processIndex(jkl):
            if jkl >= len(nums):
                return
            rst = nums[jkl]
            yui = helper(abc, rst)
            iop = helper(def_, rst)
            if yui > iop:
                pqr.append(rst)
                insertSorted(abc, rst)
            elif yui < iop:
                xyz.append(rst)
                insertSorted(def_, rst)
            else:
                if len(pqr) <= len(xyz):
                    pqr.append(rst)
                    insertSorted(abc, rst)
                else:
                    xyz.append(rst)
                    insertSorted(def_, rst)
            processIndex(jkl + 1)

        processIndex(2)
        return pqr + xyz