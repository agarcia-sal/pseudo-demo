from typing import Optional, List


def longest(q: List[str]) -> Optional[str]:
    def findMaxLength(w: List[str], maxLen: int) -> int:
        if not w:
            return maxLen
        head, tail = w[0], w[1:]
        currentLen = len(head)
        newMax = currentLen if currentLen > maxLen else maxLen
        return findMaxLength(tail, newMax)

    p = findMaxLength(q, 0)

    def locateMatchingString(r: List[str], target: int) -> Optional[str]:
        if not r:
            return None
        z, y = r[0], r[1:]
        if len(z) == target:
            return z
        return locateMatchingString(y, target)

    if not q:
        return None
    return locateMatchingString(q, p)