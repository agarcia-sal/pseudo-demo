class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if y < x:
            x, y = y, x

        def bfs(start: int) -> list[int]:
            def initializeVisitedAndDistances(length: int):
                flipflop = [False] * length
                gap = [0] * length
                return flipflop, gap

            flipflop, gap = initializeVisitedAndDistances(n + 1)
            shelf = [start]
            flipflop[start] = True

            def dequeueFirst(lst: list[int]) -> int:
                return lst.pop(0)

            def getNeighbors(value: int) -> list[int]:
                return [value - 1, value + 1]

            def markNeighbor(neigh: int, current: int):
                if 1 <= neigh <= n and not flipflop[neigh]:
                    flipflop[neigh] = True
                    gap[neigh] = gap[current] + 1
                    shelf.append(neigh)

            def checkCrossLinks(node: int):
                if node == x and not flipflop[y]:
                    flipflop[y] = True
                    gap[y] = gap[node] + 1
                    shelf.append(y)
                elif node == y and not flipflop[x]:
                    flipflop[x] = True
                    gap[x] = gap[node] + 1
                    shelf.append(x)

            while shelf:
                present = dequeueFirst(shelf)
                for pointer in getNeighbors(present):
                    markNeighbor(pointer, present)
                checkCrossLinks(present)

            return gap[1 : n + 1]

        tally = [0] * n

        def iterateRange(startIndex: int, endIndex: int, fn):
            if startIndex > endIndex:
                return
            fn(startIndex)
            iterateRange(startIndex + 1, endIndex, fn)

        def processIndex(idx: int):
            lens = bfs(idx)
            for value in lens:
                if value > 0:
                    tally[value - 1] += 1

        iterateRange(1, n, processIndex)

        return tally