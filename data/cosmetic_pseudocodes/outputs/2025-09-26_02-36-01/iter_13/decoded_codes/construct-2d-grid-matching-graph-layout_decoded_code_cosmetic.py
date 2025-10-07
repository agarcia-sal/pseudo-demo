class Solution:
    def constructGridLayout(self, n, edges):
        def buildAdjacency(size, connections):
            matrix = [[] for _ in range(size)]

            def RECURSIVE_FILL(pairList, graph, idx):
                if idx >= len(pairList):
                    return
                a, b = pairList[idx]
                graph[a].append(b)
                graph[b].append(a)
                RECURSIVE_FILL(pairList, graph, idx + 1)

            RECURSIVE_FILL(connections, matrix, 0)
            return matrix

        def findDegrees(graph):
            degreeMap = [-1] * 5

            def helperProcess(index):
                if index == len(graph):
                    return
                currentLength = len(graph[index])
                degreeMap[currentLength] = index
                helperProcess(index + 1)

            helperProcess(0)
            return degreeMap

        def searchRow(node, visitedNodes, graph):
            path = []
            prevNode = node
            if not graph[node]:
                return path
            currentNode = graph[node][0]
            while len(graph[currentNode]) > 2:
                path.append(currentNode)
                for candidate in graph[currentNode]:
                    if candidate != prevNode and len(graph[candidate]) < 4:
                        prevNode = currentNode
                        currentNode = candidate
                        break
                else:
                    # In case no candidate found, break to avoid infinite loop
                    break
            path.append(currentNode)
            return path

        def getRow(degreeMapping, graph):
            if degreeMapping[1] != -1:
                return [degreeMapping[1]]
            elif degreeMapping[4] == -1:
                candidate = degreeMapping[2]
                for neighbor in graph[candidate]:
                    if len(graph[neighbor]) == 2:
                        return [candidate, neighbor]
                return []
            else:
                startNode = degreeMapping[2]
                partialPath = [startNode]
                extendedPath = searchRow(startNode, partialPath, graph)
                return partialPath + extendedPath

        def markVisited(nodes, visitation):
            for element in nodes:
                visitation[element] = True

        def findNextLayer(currentLayer, visitation, graph):
            nextLayer = []
            for element in currentLayer:
                for neighbor in graph[element]:
                    if not visitation[neighbor]:
                        nextLayer.append(neighbor)
                        break
            return nextLayer

        adjacency = buildAdjacency(n, edges)
        degreeList = findDegrees(adjacency)
        baseRow = getRow(degreeList, adjacency)
        resultGrid = [baseRow]
        visitedFlags = [False] * n

        def repeatLayers(count, row, visited, grid, accumulator):
            if count <= 0:
                return
            markVisited(row, visited)
            nextRow = findNextLayer(row, visited, grid)
            accumulator.append(nextRow)
            repeatLayers(count - 1, nextRow, visited, grid, accumulator)

        iterations = (n // len(baseRow)) - 1 if baseRow else 0
        repeatLayers(iterations, baseRow, visitedFlags, adjacency, resultGrid)

        return resultGrid