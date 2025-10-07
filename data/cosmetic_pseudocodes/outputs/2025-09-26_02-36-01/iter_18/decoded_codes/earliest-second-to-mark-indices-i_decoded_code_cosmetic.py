from typing import List, Set

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        p = len(nums)
        q = len(changeIndices)

        def can_mark_by_second(u: int) -> bool:
            v = [-1] * p  # Map index to earliest second it was changed
            w = 0
            while w < u:
                x = changeIndices[w] - 1  # zero-based index
                v[x] = w
                w += 1

            aa = 0  # Current available count to cover nums
            ab: Set[int] = set()  # Set of indices successfully marked

            ac = 0
            while True:
                if ac >= u:
                    break
                ad = changeIndices[ac] - 1

                if ad not in ab:
                    if v[ad] == ac:
                        if nums[ad] <= aa:
                            aa -= nums[ad]
                            ab.add(ad)
                        else:
                            return False
                    else:
                        aa += 1
                else:
                    aa += 1
                ac += 1

            if len(ab) == p:
                return True
            else:
                return False

        ag, ah = 0, q + 1
        while ag < ah:
            ai = (ag + ah) // 2
            if can_mark_by_second(ai):
                ah = ai
            else:
                ag += 1

        return ag if ag <= q else -1