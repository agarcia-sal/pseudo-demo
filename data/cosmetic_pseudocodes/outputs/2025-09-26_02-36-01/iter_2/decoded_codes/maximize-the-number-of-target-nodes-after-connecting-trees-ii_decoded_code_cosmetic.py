from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        graphA = defaultdict(list)
        graphB = defaultdict(list)

        idx1 = 0
        while idx1 < len(edges1):
            nodeX, nodeY = edges1[idx1][0], edges1[idx1][1]
            graphA[nodeX].append(nodeY)
            graphA[nodeY].append(nodeX)
            idx1 += 1

        idx2 = 0
        while idx2 < len(edges2):
            nodeP, nodeQ = edges2[idx2][0], edges2[idx2][1]
            graphB[nodeP].append(nodeQ)
            graphB[nodeQ].append(nodeP)
            idx2 += 1

        sizeA = len(graphA)
        sizeB = len(graphB)

        def bfs(treeStructure, origin):
            countEven = 0
            countOdd = 0
            firstQueue = deque([(origin, 0)])
            seenSet = {origin}

            while firstQueue:
                currentNode, distance = firstQueue.popleft()
                if distance % 2 == 0:
                    countEven += 1
                else:
                    countOdd += 1

                neighborsArray = treeStructure[currentNode]
                idxNeighbor = 0
                while idxNeighbor < len(neighborsArray):
                    adjacentNode = neighborsArray[idxNeighbor]
                    if adjacentNode not in seenSet:
                        seenSet.add(adjacentNode)
                        firstQueue.append((adjacentNode, distance + 1))
                    idxNeighbor += 1

            return countEven, countOdd

        countsA = []
        indexA = 0
        while indexA < sizeA:
            countsA.append(bfs(graphA, indexA))
            indexA += 1

        countsB = []
        indexB = 0
        while indexB < sizeB:
            countsB.append(bfs(graphB, indexB))
            indexB += 1

        finalList = []
        outerIdx = 0
        while outerIdx < sizeA:
            evenCountA, oddCountA = countsA[outerIdx][0], countsA[outerIdx][1]
            maximumTargets = 0
            innerIdx = 0
            while innerIdx < sizeB:
                evenCountB, oddCountB = countsB[innerIdx][0], countsB[innerIdx][1]
                if (outerIdx == innerIdx) or ((outerIdx % 2) == (innerIdx % 2)):
                    possibleTargets = evenCountB
                else:
                    possibleTargets = oddCountB

                if possibleTargets > maximumTargets:
                    maximumTargets = possibleTargets
                innerIdx += 1
            finalList.append(evenCountA + maximumTargets)
            outerIdx += 1

        return finalList