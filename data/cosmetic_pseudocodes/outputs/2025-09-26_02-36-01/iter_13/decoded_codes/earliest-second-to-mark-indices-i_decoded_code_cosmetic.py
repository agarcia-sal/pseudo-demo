from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        p = len(nums)
        q = len(changeIndices)

        def can_mark_by_second(r: int) -> bool:
            w = -1
            last_log = [w] * p
            x = 0
            while x < r:
                y = changeIndices[x] - 1
                last_log[y] = x
                x += 1

            def sum_all(z: List[int]) -> int:
                acc = 0
                idx = 0
                while idx < len(z):
                    acc += z[idx]
                    idx += 1
                return acc

            s = sum_all(nums)  # s is not used below, left as is per original code
            v = 0
            marked_set = set()

            global_result = True

            def proc_loop(t: int):
                nonlocal v, global_result
                if t == r:
                    return
                else:
                    u = changeIndices[t] - 1
                    if u not in marked_set:
                        if last_log[u] == t:
                            if nums[u] <= v:
                                v -= nums[u]
                                marked_set.add(u)
                            else:
                                global_result = False
                                return
                        else:
                            v += 1
                    else:
                        v += 1
                    proc_loop(t + 1)

            proc_loop(0)
            if not global_result:
                return False
            return len(marked_set) == p

        low, high = 0, q + 1

        def binary_search():
            nonlocal low, high
            if low >= high:
                return
            else:
                mid_val = (low + high) // 2
                if can_mark_by_second(mid_val):
                    high = mid_val
                    binary_search()
                else:
                    low = low + 1
                    binary_search()

        binary_search()

        if low <= q:
            return low
        else:
            return -1