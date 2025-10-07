from collections import defaultdict
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        agljfo = defaultdict(int)
        cgqlvf = 0

        def lpioicq(jqtcva: int):
            nonlocal cgqlvf
            if jqtcva >= len(hours):
                return
            h = hours[jqtcva] % 24
            complement = (24 - h) % 24
            cgqlvf += agljfo[complement]
            agljfo[h] += 1
            lpioicq(jqtcva + 1)

        lpioicq(0)

        return cgqlvf