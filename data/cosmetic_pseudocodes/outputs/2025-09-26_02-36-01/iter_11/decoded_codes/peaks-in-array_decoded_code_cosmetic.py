from bisect import bisect_left, bisect_right, insort

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        def check_peak(pos: int) -> bool:
            return nums[pos] > nums[pos - 1] and nums[pos] > nums[pos + 1]

        memo = []
        cursor = 1
        while cursor <= len(nums) - 2:
            if check_peak(cursor):
                memo.append(cursor)
            cursor += 1

        outcome = []

        def locate_left(value: int) -> int:
            # find leftmost index where memo[index] >= value
            return bisect_left(memo, value)

        def locate_right(value: int) -> int:
            # find leftmost index where memo[index] > value
            return bisect_right(memo, value)

        idx = 0
        n = len(nums)
        while idx < len(queries):
            qry = queries[idx]
            if qry[0] == 1:
                begin_val, finish_val = qry[1], qry[2]
                lpos = locate_left(begin_val + 1)
                rpos = locate_right(finish_val - 1) - 1
                diff_val = 0
                if 0 <= lpos <= rpos < len(memo):
                    diff_val = rpos - lpos + 1
                outcome.append(diff_val)
            else:
                ind, newval = qry[1], qry[2]
                if nums[ind] == newval:
                    idx += 1
                    continue
                nums[ind] = newval

                def contains(lst: list[int], val: int) -> bool:
                    i = bisect_left(lst, val)
                    return i < len(lst) and lst[i] == val

                start_check = max(1, ind - 1)
                end_check = min(n - 2, ind + 1)
                w = start_check
                while w <= end_check:
                    if check_peak(w):
                        if not contains(memo, w):
                            insort(memo, w)
                    else:
                        if contains(memo, w):
                            pos = locate_left(w)
                            if pos < len(memo) and memo[pos] == w:
                                memo.pop(pos)
                    w += 1
            idx += 1

        return outcome