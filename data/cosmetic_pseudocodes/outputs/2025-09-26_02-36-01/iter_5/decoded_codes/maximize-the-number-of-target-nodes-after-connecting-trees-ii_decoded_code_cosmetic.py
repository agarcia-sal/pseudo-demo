from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        adjacencyMap1 = defaultdict(list)
        adjacencyMap2 = defaultdict(list)

        def buildGraph(edgeList, graph):
            if not edgeList:
                return
            currentEdge = edgeList[0]
            graph[currentEdge[0]].append(currentEdge[1])
            graph[currentEdge[1]].append(currentEdge[0])
            buildGraph(edgeList[1:], graph)

        buildGraph(edges1, adjacencyMap1)
        buildGraph(edges2, adjacencyMap2)

        count1 = len(adjacencyMap1)
        count2 = len(adjacencyMap2)

        def bfs(graphStructure, origin):
            accumulateEven = 0
            accumulateOdd = 0
            processingQueue = deque([(origin, 0)])
            visitedSet = {origin}

            def processQueue(queue):
                nonlocal accumulateEven, accumulateOdd
                if not queue:
                    return accumulateEven, accumulateOdd

                currentNode, currentDistance = queue.popleft()
                if currentDistance % 2 == 0:
                    accumulateEven += 1
                else:
                    accumulateOdd += 1

                def iterateNeighbors(neighborsList):
                    if not neighborsList:
                        return
                    nextNeighbor = neighborsList[0]
                    if nextNeighbor not in visitedSet:
                        visitedSet.add(nextNeighbor)
                        queue.append((nextNeighbor, currentDistance + 1))
                    iterateNeighbors(neighborsList[1:])

                iterateNeighbors(graphStructure[currentNode])
                return processQueue(queue)

            return processQueue(processingQueue)

        countsList1 = []

        def fillCounts1(index):
            if index == count1:
                return
            countsPair = bfs(adjacencyMap1, index)
            countsList1.append(countsPair)
            fillCounts1(index + 1)

        fillCounts1(0)

        countsList2 = []

        def fillCounts2(index):
            if index == count2:
                return
            countsPair = bfs(adjacencyMap2, index)
            countsList2.append(countsPair)
            fillCounts2(index + 1)

        fillCounts2(0)

        finalResults = []

        def computeResults(i):
            if i == count1:
                return
            evenCountI, oddCountI = countsList1[i]
            peakTarget = 0

            def innerLoop(j):
                nonlocal peakTarget
                if j == count2:
                    return
                evenCountJ, oddCountJ = countsList2[j]
                if i == j or (i % 2) == (j % 2):
                    candidateTargets = evenCountJ
                else:
                    candidateTargets = oddCountJ

                if candidateTargets > peakTarget:
                    peakTarget = candidateTargets

                innerLoop(j + 1)

            innerLoop(0)
            finalResults.append(evenCountI + peakTarget)
            computeResults(i + 1)

        computeResults(0)

        return finalResults