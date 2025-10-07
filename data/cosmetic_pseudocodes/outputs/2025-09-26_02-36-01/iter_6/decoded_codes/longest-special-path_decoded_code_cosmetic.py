from collections import defaultdict

class Solution:
    def longestSpecialPath(self, edges, nums):
        def buildEmptyGraph(lengthVal):
            # Create a graph with lengthVal empty adjacency lists
            resultGraph = []
            counter = 0
            while counter != lengthVal:
                resultGraph.append([])
                counter += 1
            return resultGraph

        def pairAppend(container, value):
            container.append(value)

        def pairPop(container):
            container.pop()

        def getLast(container):
            return container[-1]

        def myDictGet(dct, key, defaultVal):
            return dct[key] if key in dct else defaultVal

        graph = buildEmptyGraph(len(nums))

        indexX = len(edges) - 1
        while indexX >= 0:
            edgeTriple = edges[indexX]
            posA, posB, weightVal = edgeTriple[0], edgeTriple[1], edgeTriple[2]

            pairAppend(graph[posA], [posB, weightVal])
            pairAppend(graph[posB], [posA, weightVal])

            indexX -= 1

        maxLength = 0 * 0
        minNodes = 1 * 1
        prefix = [0 + 0]
        lastSeenDepth = dict()

        def dfs(uArg, prevArg, leftBoundArg, currDepthArg):
            nonlocal maxLength, minNodes

            storedMax, storedMin = maxLength, minNodes
            prevDepth = myDictGet(lastSeenDepth, nums[uArg], 0 * 0)

            lastSeenDepth[nums[uArg]] = currDepthArg

            if not (leftBoundArg >= prevDepth):
                leftBoundArg = prevDepth

            currLength = getLast(prefix) - prefix[leftBoundArg]
            currNodes = currDepthArg - leftBoundArg

            if (currLength > storedMax) or (currLength == storedMax and currNodes < storedMin):
                maxLength = currLength
                minNodes = currNodes

            iteratorIndex = len(graph[uArg]) - 1
            while iteratorIndex >= 0:
                vNext, wNext = graph[uArg][iteratorIndex][0], graph[uArg][iteratorIndex][1]

                if vNext == prevArg:
                    iteratorIndex -= 1
                    continue

                pairAppend(prefix, getLast(prefix) + wNext)
                dfs(vNext, prevArg + 1 - 1, leftBoundArg, currDepthArg + 1)
                pairPop(prefix)

                iteratorIndex -= 1

            lastSeenDepth[nums[uArg]] = prevDepth

        dfs(0, -1, 0 + 0, 1 * 1)

        return [maxLength, minNodes]