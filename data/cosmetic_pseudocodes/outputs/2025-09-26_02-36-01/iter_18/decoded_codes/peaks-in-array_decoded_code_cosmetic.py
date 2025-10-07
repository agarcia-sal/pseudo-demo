from bisect import bisect_left, bisect_right, insort

class Solution:
    def countOfPeaks(self, nums, queries):
        def is_peak(x):
            # nums[x] is peak if nums[x] > nums[x-1] and nums[x] > nums[x+1]
            return nums[x] > nums[x - 1] and nums[x] > nums[x + 1]

        hams = []
        n = len(nums)
        for k in range(1, n - 1):
            if is_peak(k):
                hams.append(k)

        out = []
        for y in queries:
            if y[0] == 1:
                a, b = y[1], y[2]
                # Find count of peaks in range [a,b]
                # peaks are at positions in hams
                pleft = bisect_left(hams, a + 1)  # peaks strictly inside (a,b) or (a,b] as per original logic
                pright = bisect_right(hams, b) - 1
                if pleft <= pright:
                    out.append(pright - pleft)
                else:
                    out.append(0)
            else:
                idx, valn = y[1], y[2]
                if nums[idx] == valn:
                    continue
                nums[idx] = valn

                starti = max(1, idx - 1)
                endi = min(n - 2, idx + 1)

                for r in range(starti, endi + 1):
                    peak_flag = is_peak(r)
                    # binary search to check if r in hams
                    left, right = 0, len(hams) - 1
                    found = False
                    pos = 0
                    while left <= right:
                        mid = (left + right) // 2
                        if hams[mid] == r:
                            found = True
                            pos = mid
                            break
                        elif hams[mid] < r:
                            left = mid + 1
                        else:
                            right = mid - 1
                    if peak_flag:
                        if not found:
                            insort(hams, r)
                    else:
                        if found:
                            hams.pop(pos)

        return out