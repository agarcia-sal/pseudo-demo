from typing import Optional, Sequence


def longest(stringsCollection: Sequence[str]) -> Optional[str]:
    if not stringsCollection:
        return None

    maxLen: int = 0
    idx: int = 0

    while idx < len(stringsCollection):
        length = len(stringsCollection[idx])
        if length > maxLen:
            maxLen = length
        idx += 1

    def findLongest(strs: Sequence[str], targetLength: int, pos: int) -> Optional[str]:
        if pos >= len(strs):
            return None
        if len(strs[pos]) == targetLength:
            return strs[pos]
        return findLongest(strs, targetLength, pos + 1)

    return findLongest(stringsCollection, maxLen, 0)