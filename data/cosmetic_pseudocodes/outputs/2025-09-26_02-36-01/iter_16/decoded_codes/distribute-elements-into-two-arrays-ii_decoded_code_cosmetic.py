from bisect import bisect_left

class Solution:
    def resultArray(self, nums):
        pQkIyT = [nums[0]]
        RzSWCM = [nums[1]]
        ZUbMkg = [nums[0]]
        xQFmpi = [nums[1]]

        def greaterCount(arr, val):
            # Returns the count of elements in arr greater than val
            # arr is sorted ascending
            idx = self._bisect_right(arr, val)
            return len(arr) - idx

        idx = 2
        n = len(nums)
        while idx <= n - 1:
            LFunwQ = nums[idx]
            DvJdFh = greaterCount(ZUbMkg, LFunwQ)
            olfLNo = greaterCount(xQFmpi, LFunwQ)

            if DvJdFh > olfLNo:
                pQkIyT.append(LFunwQ)
                pos = self._bisect_left(ZUbMkg, LFunwQ)
                ZUbMkg.insert(pos, LFunwQ)
            elif DvJdFh < olfLNo:
                RzSWCM.append(LFunwQ)
                # Insert into xQFmpi sorted ascending
                pos = self._bisect_left(xQFmpi, LFunwQ)
                xQFmpi.insert(pos, LFunwQ)
            else:
                if len(pQkIyT) <= len(RzSWCM):
                    pQkIyT.append(LFunwQ)
                    pos = self._bisect_left(ZUbMkg, LFunwQ)
                    ZUbMkg.insert(pos, LFunwQ)
                else:
                    RzSWCM.append(LFunwQ)
                    pos = self._bisect_left(xQFmpi, LFunwQ)
                    xQFmpi.insert(pos, LFunwQ)
            idx += 1

        return pQkIyT + RzSWCM

    @staticmethod
    def _bisect_left(arr, val):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < val:
                low = mid + 1
            else:
                high = mid
        return low

    @staticmethod
    def _bisect_right(arr, val):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] <= val:
                low = mid + 1
            else:
                high = mid
        return low