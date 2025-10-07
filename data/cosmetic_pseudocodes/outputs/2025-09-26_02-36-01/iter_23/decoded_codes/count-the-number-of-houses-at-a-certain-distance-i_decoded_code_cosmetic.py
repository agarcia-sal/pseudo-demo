from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        deltaW = 0
        umax = n
        retval = [0] * n  # list with n zeros

        def traverseBFS(start: int):
            flagList = [False] * (umax + 1)
            distArr = [0] * (umax + 1)
            deqContainer = deque([start])
            flagList[start] = True

            while deqContainer:
                currItem = deqContainer.popleft()
                adjCandidates = [currItem - 1, currItem + 1]

                for node in adjCandidates:
                    if 1 <= node <= umax and not flagList[node]:
                        flagList[node] = True
                        distArr[node] = distArr[currItem] + 1
                        deqContainer.append(node)

                # Check conditions for special connections between x and y
                if currItem == x and not flagList[y]:
                    flagList[y] = True
                    distArr[y] = distArr[currItem] + 1
                    deqContainer.append(y)
                if currItem == y and not flagList[x]:
                    flagList[x] = True
                    distArr[x] = distArr[currItem] + 1
                    deqContainer.append(x)

            for idx in range(1, umax + 1):
                if distArr[idx] > 0:
                    retval[distArr[idx] - 1] += 1

        def loopHelper(iterator: int):
            if iterator > umax:
                return
            traverseBFS(iterator)
            loopHelper(iterator + 1)

        loopHelper(1)
        return retval