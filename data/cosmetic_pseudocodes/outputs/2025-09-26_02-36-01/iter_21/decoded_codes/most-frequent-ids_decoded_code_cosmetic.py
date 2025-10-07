from collections import deque, defaultdict
from typing import List

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        u = 0
        v = defaultdict(int)
        w = deque()
        x = []

        def z(a: int, b: int) -> int:
            return a + b

        def y() -> bool:
            # This function is defined but never used or required by the pseudocode,
            # implemented faithfully as is, but will not affect result.
            while True:
                if len(w) == 0:
                    break
                if -w[0][0] == v[w[0][1]]:
                    return True
                else:
                    return False
            return False

        def t():
            nonlocal u
            if u >= len(nums):
                return
            v[nums[u]] = z(v[nums[u]], freq[u])
            s = -v[nums[u]]
            q = nums[u]
            w.appendleft((s, q))

            while True:
                if len(w) == 0:
                    break
                if not (-w[0][0] != v[w[0][1]]):
                    break
                w.popleft()

            if len(w) > 0:
                x.append(-w[0][0])
            else:
                x.append(0)

            u += 1
            t()

        t()
        return x