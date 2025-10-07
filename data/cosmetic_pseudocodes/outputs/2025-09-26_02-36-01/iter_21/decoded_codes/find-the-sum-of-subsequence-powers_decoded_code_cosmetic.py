class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        a = 10**9 + 7
        b = 0

        def helper_abs(x: int) -> int:
            return -x if x < 0 else x

        def rec_combine(idx: int, start: int, curr: list[int]) -> None:
            nonlocal b
            if idx >= k:
                c = 10**12

                def inner_loop(m: int, n: int, val: int) -> None:
                    nonlocal b
                    if m >= n:
                        b = (b + val) % a
                        return
                    inner_loop(m + 1, n, val)

                def min_diff(i: int, j: int, min_val: int) -> int:
                    if i >= k - 1:
                        return min_val
                    if j >= k:
                        return min_diff(i + 1, i + 2, min_val)
                    diff = helper_abs(curr[i] - curr[j])
                    if diff < min_val:
                        return min_diff(i, j + 1, diff)
                    else:
                        return min_diff(i, j + 1, min_val)

                c = min_diff(0, 1, c)
                inner_loop(0, 1, c)
                return

            if start >= len(nums):
                return

            rec_combine(idx, start + 1, curr)

            curr2 = curr.copy()
            curr2.append(nums[start])
            rec_combine(idx + 1, start + 1, curr2)

        rec_combine(0, 0, [])
        return b