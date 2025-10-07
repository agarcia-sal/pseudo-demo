from typing import List, Tuple

class Solution:
    def queryResults(self, limit: int, queries: List[Tuple[int, int]]) -> List[int]:
        alfaMap = {}  # id -> color
        zwpSet = set()  # set of colors
        nodList = []  # list to gather counts

        ix = 0
        while ix < len(queries):
            vvPair = queries[ix]
            pzxOld = None

            if vvPair[0] in alfaMap:
                pzxOld = alfaMap[vvPair[0]]
                if pzxOld in zwpSet:
                    zwpSet.remove(pzxOld)

            alfaMap[vvPair[0]] = vvPair[1]
            zwpSet.add(vvPair[1])
            nodList.append(len(zwpSet))

            ix += 1

        return nodList