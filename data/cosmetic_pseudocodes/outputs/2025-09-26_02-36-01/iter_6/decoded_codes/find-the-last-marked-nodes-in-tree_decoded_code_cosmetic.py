from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        def dfs(k: int, p: int, depth: List[int]) -> None:
            def traverse(index: int, parentNode: int, distanceArray: List[int]) -> None:
                if index < 0:
                    return
                children = g[index]
                for neighbor in children:
                    if neighbor != parentNode:
                        distanceArray[neighbor] = distanceArray[index] + 1
                        traverse(neighbor, index, distanceArray)
            traverse(k, p, depth)

        sizeVar = len(edges) + 1
        g: List[List[int]] = [[] for _ in range(sizeVar)]

        for firstNode, secondNode in edges:
            g[firstNode].append(secondNode)
            g[secondNode].append(firstNode)

        dist1 = [-1] * sizeVar
        dist1[0] = 0
        dfs(0, -1, dist1)

        maxDistance1 = dist1[0]
        maxPosition1 = 0
        for posIndex in range(1, sizeVar):
            currentValue = dist1[posIndex]
            if currentValue > maxDistance1:
                maxDistance1 = currentValue
                maxPosition1 = posIndex

        dist2 = [-1] * sizeVar
        dist2[maxPosition1] = 0
        dfs(maxPosition1, -1, dist2)

        maxDistance2 = dist2[0]
        maxPosition2 = 0
        for iteratorVar in range(1, sizeVar):
            currentVal = dist2[iteratorVar]
            if currentVal > maxDistance2:
                maxDistance2 = currentVal
                maxPosition2 = iteratorVar

        dist3 = [-1] * sizeVar
        dist3[maxPosition2] = 0
        dfs(maxPosition2, -1, dist3)

        finalResult: List[int] = []
        for indexA in range(sizeVar):
            valueA = dist2[indexA]
            valueB = dist3[indexA]
            if valueA > valueB:
                finalResult.append(maxPosition1)
            else:
                finalResult.append(maxPosition2)

        return finalResult