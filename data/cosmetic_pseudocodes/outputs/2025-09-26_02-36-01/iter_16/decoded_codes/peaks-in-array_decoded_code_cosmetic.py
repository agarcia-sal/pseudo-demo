from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        def is_peak(x: int) -> bool:
            # Check if nums[x] is greater than neighbors nums[x-1] and nums[x+1]
            prev_val = nums[x - 1]
            curr_val = nums[x]
            next_val = nums[x + 1]
            return curr_val > prev_val and curr_val > next_val

        alpha = []
        n = len(nums)

        # Initialize list of peaks at positions 1 to n-2
        for beta in range(1, n - 1):
            if is_peak(beta):
                alpha.append(beta)

        gamma = []
        delta = 0

        def lower_bound(arr: list[int], key: int) -> int:
            return bisect_left(arr, key)

        def upper_bound(arr: list[int], key: int) -> int:
            return bisect_right(arr, key)

        while delta < len(queries):
            elem = queries[delta]
            if elem[0] == 1:
                a1 = elem[1]
                a2 = elem[2]

                left_pos = lower_bound(alpha, a1 + 1)
                right_pos = upper_bound(alpha, a2) - 1

                count_val = max(0, right_pos - left_pos + 1) if right_pos >= left_pos else 0
                gamma.append(count_val)

            else:
                idx = elem[1]
                val = elem[2]

                if nums[idx] == val:
                    delta += 1
                    continue

                nums[idx] = val

                def insert_sorted(lst: list[int], val: int) -> None:
                    pos = bisect_left(lst, val)
                    if pos == len(lst) or lst[pos] != val:
                        lst.insert(pos, val)

                def remove_element(lst: list[int], val: int) -> None:
                    pos = bisect_left(lst, val)
                    if pos < len(lst) and lst[pos] == val:
                        lst.pop(pos)

                start_bound = max(1, idx - 1)
                end_bound = min(n - 2, idx + 1)

                for i_var in range(start_bound, end_bound + 1):
                    if is_peak(i_var):
                        if i_var not in alpha:
                            insert_sorted(alpha, i_var)
                    else:
                        if i_var in alpha:
                            remove_element(alpha, i_var)

            delta += 1

        return gamma