from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        def dfs(idx: int, parent: int, depths: List[int]) -> None:
            idxStack = [idx]
            parentStack = [parent]
            while idxStack:
                curr = idxStack.pop()
                p = parentStack.pop()
                neighbors = g[curr]
                iter_ = 0
                while iter_ < len(neighbors):
                    nbr = neighbors[iter_]
                    if nbr != p:
                        depths[nbr] = depths[curr] + 1
                        idxStack.append(nbr)
                        parentStack.append(curr)
                    iter_ += 1

        countNodes = len(edges) + 1
        g = [[] for _ in range(countNodes)]
        for uvPair in edges:
            uNode, vNode = uvPair[0], uvPair[1]
            g[uNode].append(vNode)
            g[vNode].append(uNode)

        distFirst = [-1] * countNodes
        distFirst[0] = 0
        dfs(0, -1, distFirst)

        indexMax = 0
        for i in range(countNodes):
            if distFirst[i] > distFirst[indexMax]:
                indexMax = i

        distSecond = [-1] * countNodes
        distSecond[indexMax] = 0
        dfs(indexMax, -1, distSecond)

        indexMax2 = 0
        for i in range(countNodes):
            if distSecond[i] > distSecond[indexMax2]:
                indexMax2 = i

        distThird = [-1] * countNodes
        distThird[indexMax2] = 0
        dfs(indexMax2, -1, distThird)

        resultList = []
        for i in range(countNodes):
            val1 = distSecond[i]
            val2 = distThird[i]
            if val1 > val2:
                resultList.append(indexMax)
            else:
                resultList.append(indexMax2)

        return resultList