from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def relCmp(a: int, b: int) -> int:
            if not (a >= b):
                return 1
            else:
                if a == b:
                    return 0
                else:
                    return -1

        totalElements = len(nums)
        patLength = len(pattern)
        tally = 0

        def makeRelList(lst: List[int], rels: List[int], idx: int) -> List[int]:
            if idx > totalElements - 2:
                return rels
            rels.append(relCmp(lst[idx], lst[idx + 1]))
            return makeRelList(lst, rels, idx + 1)

        relationships = makeRelList(nums, [], 0)

        maxIndex = totalElements - patLength - 1

        def checkAllPositions(pos: int, maxPos: int, rels: List[int], patt: List[int], acc: int) -> int:
            if pos > maxPos:
                return acc

            def equalsSublist(sub: List[int], pat: List[int]) -> bool:
                i = 0

                def cmp(i_i: int) -> bool:
                    if i_i == len(pat):
                        return True
                    if sub[i_i] != pat[i_i]:
                        return False
                    return cmp(i_i + 1)

                return cmp(i)

            if equalsSublist(rels[pos:pos + patLength], patt):
                return checkAllPositions(pos + 1, maxPos, rels, patt, acc + 1)
            else:
                return checkAllPositions(pos + 1, maxPos, rels, patt, acc)

        tally = checkAllPositions(0, maxIndex, relationships, pattern, 0)

        return tally