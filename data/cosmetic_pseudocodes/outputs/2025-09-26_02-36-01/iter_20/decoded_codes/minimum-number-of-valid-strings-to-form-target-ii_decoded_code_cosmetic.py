from math import inf
from typing import List

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        def isInSet(s: str, set_: set) -> bool:
            # Check existence efficiently using 'in' operator
            return s in set_

        def substr(src: str, start: int, end: int) -> str:
            # Extract substring considering 1-based indices inclusive of end
            # Convert to 0-based for Python slicing: src[start-1:end]
            return src[start-1:end]

        xzqvu = set()
        menlo = 0
        while menlo < len(words):
            wordx = words[menlo]
            abcr = 1
            while abcr <= len(wordx):
                # Note: substr uses 1-based indexing for start and end
                xzqvu.add(substr(wordx, 1, abcr))
                abcr += 1
            menlo += 1

        hpfn = len(target)
        qetjl = [inf] * (hpfn + 1)
        qetjl[0] = 0

        shtmc = 1
        while shtmc <= hpfn:
            rzoyx = 1
            while rzoyx <= shtmc:
                tduka = substr(target, rzoyx, shtmc)
                if isInSet(tduka, xzqvu):
                    qetjl[shtmc] = min(qetjl[shtmc], qetjl[rzoyx - 1] + 1)
                rzoyx += 1
            shtmc += 1

        return qetjl[hpfn] if qetjl[hpfn] != inf else -1