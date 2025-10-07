from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        alpha = defaultdict(list)
        n = len(edges)

        def buildTree(k: int, n: int) -> None:
            if k < n:
                x, y = edges[k]
                alpha[x].append(y)
                alpha[y].append(x)
                buildTree(k + 1, n)

        counterResult = 1

        def walker(node: int, prev: int) -> int:
            nonlocal counterResult
            localCount = 1
            allSiblingsMatch = True
            children = alpha[node]

            def iterateChildren(idx: int):
                nonlocal localCount, allSiblingsMatch
                if idx < len(children):
                    nbr = children[idx]
                    if nbr != prev:
                        retVal = walker(nbr, node)
                        if retVal == 0:
                            allSiblingsMatch = False
                        elif colors[nbr] == colors[node]:
                            localCount += retVal
                        else:
                            allSiblingsMatch = False
                    iterateChildren(idx + 1)

            iterateChildren(0)

            if allSiblingsMatch:
                if counterResult < localCount:
                    counterResult = localCount
                return localCount
            else:
                return 0

        edgeCount = len(edges)
        buildTree(0, edgeCount)
        _ = walker(0, -1)
        return counterResult