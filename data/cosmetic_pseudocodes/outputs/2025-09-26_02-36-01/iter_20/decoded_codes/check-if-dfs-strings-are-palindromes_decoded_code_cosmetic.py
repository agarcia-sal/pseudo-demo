from typing import List, Tuple, Dict

class Hashing:
    def __init__(self, s: List[str], base: int, mod: int):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)

        def multiplyModulo(a: int, b: int) -> int:
            return (a * b) % self.mod

        def addModulo(a: int, b: int) -> int:
            return (a + b) % self.mod

        def loopBuilder(current: int) -> None:
            if current > n:
                return
            tempE = self.h[current - 1]
            tempF = multiplyModulo(tempE, base)
            tempG = ord(s[current - 1])
            self.h[current] = addModulo(tempF, tempG)
            tempH = self.p[current - 1]
            self.p[current] = multiplyModulo(tempH, base)
            loopBuilder(current + 1)

        loopBuilder(1)

    def query(self, l: int, r: int) -> int:
        def modSubtraction(x: int, y: int) -> int:
            diff = x - y
            if diff < 0:
                diff += self.mod
            return diff

        def modMultiplication(x: int, y: int) -> int:
            return (x * y) % self.mod

        diffVal = modSubtraction(self.h[r], self.h[l - 1])
        powerVal = self.p[r - l + 1]
        productVal = modMultiplication(diffVal, powerVal)
        return productVal % self.mod


class Solution:
    def findAnswer(self, parent: List[int], s: List[str]) -> List[bool]:
        n = len(s)
        g: List[List[int]] = [[] for _ in range(n)]

        def buildGraph(current: int) -> None:
            if current >= n:
                return
            if current > 0:
                g[parent[current]].append(current)
            buildGraph(current + 1)

        buildGraph(1)

        dfsStr: List[str] = []
        pos: Dict[int, Tuple[int, int]] = {}

        def dfs(i: int) -> None:
            beginIdx = len(dfsStr) + 1
            def iterateChildren(jList: List[int], idx: int) -> None:
                if idx > len(jList):
                    return
                dfs(jList[idx - 1])
                iterateChildren(jList, idx + 1)
            iterateChildren(g[i], 1)
            dfsStr.append(s[i])
            endIdx = len(dfsStr)
            pos[i] = (beginIdx, endIdx)

        dfs(0)

        base = 33331
        mod = 998244353
        h1 = Hashing(dfsStr, base, mod)
        h2 = Hashing(dfsStr[::-1], base, mod)

        ans: List[bool] = []

        def processIndex(x: int) -> None:
            if x > n - 1:
                return
            l, r = pos[x]
            length = r - l + 1

            def halfLength() -> int:
                return length // 2

            if length % 2 == 0:
                v1 = h1.query(l, l + halfLength() - 1)
                v2 = h2.query(n - r + 1, n - r + 1 + halfLength() - 1)
            else:
                v1 = h1.query(l, l + halfLength() - 1)
                v2 = h2.query(n - r + 1, n - r + 1 + halfLength() - 1)
            ans.append(v1 == v2)
            processIndex(x + 1)

        processIndex(0)
        return ans