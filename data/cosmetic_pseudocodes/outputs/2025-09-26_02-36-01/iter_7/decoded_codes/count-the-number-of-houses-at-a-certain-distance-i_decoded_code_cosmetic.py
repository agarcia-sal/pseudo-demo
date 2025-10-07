from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        M = n
        cnt = [0] * M

        def searchBreadth(first: int):
            marked = [False] * (n + 1)
            distArr = [0] * (n + 1)
            deq = [first]
            marked[first] = True

            while deq:
                head = deq.pop(0)

                adjList = [head - 1, head + 1]
                for adj in adjList:
                    if 1 <= adj <= n and not marked[adj]:
                        marked[adj] = True
                        distArr[adj] = distArr[head] + 1
                        deq.append(adj)

                if head == x and not marked[y]:
                    marked[y] = True
                    distArr[y] = distArr[head] + 1
                    deq.append(y)

                if head == y and not marked[x]:
                    marked[x] = True
                    distArr[x] = distArr[head] + 1
                    deq.append(x)

            for pos in range(1, n + 1):
                if distArr[pos] > 0:
                    posIndex = distArr[pos] - 1
                    cnt[posIndex] += 1

        counter = 1
        while counter <= n:
            searchBreadth(counter)
            counter += 1

        return cnt