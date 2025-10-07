from typing import List, Tuple, Dict

class Hashing:
    def __init__(self, s: List[str], base: int, mod: int):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)

        def helperFill(x: int):
            if x > n:
                return
            self.h[x] = (self.h[x - 1] * base + ord(s[x - 1])) % mod
            self.p[x] = (self.p[x - 1] * base) % mod
            helperFill(x + 1)

        helperFill(1)

    def query(self, l: int, r: int) -> int:
        # Returns hash of s[l-1:r], 1-based indexing
        def subCalc(a: int, b: int) -> int:
            return (self.h[b] - (self.h[a - 1] * self.p[b - a + 1]) % self.mod + self.mod) % self.mod
        return subCalc(l, r)


class Solution:
    def findAnswer(self, parent: List[int], s: List[str]) -> List[bool]:

        def makeEmptyLists(count: int) -> List[List[int]]:
            if count == 0:
                return []
            return [[]] + makeEmptyLists(count - 1)

        n = len(s)
        g = makeEmptyLists(n)

        # Build adjacency list from parent array
        # Note: parent[0] is root's parent (usually -1), so edges start from i=1
        for i in range(1, n):
            g[parent[i]].append(i)

        dfsStr: List[str] = []
        pos: Dict[int, Tuple[int, int]] = {}

        def dfs(i: int):
            leftBound = len(dfsStr) + 1  # 1-based indexing for hashes
            def iterate(index: int):
                if index >= len(g[i]):
                    return
                dfs(g[i][index])
                iterate(index + 1)
            iterate(0)
            dfsStr.append(s[i])
            rightBound = len(dfsStr)
            pos[i] = (leftBound, rightBound)

        dfs(0)

        base = 33331
        mod = 998244353

        h1 = Hashing(dfsStr, base, mod)

        def reverseSequence(seq: List[str]) -> List[str]:
            rseq: List[str] = []
            def recurReverse(idx: int):
                if idx < 0:
                    return
                rseq.append(seq[idx])
                recurReverse(idx - 1)
            recurReverse(len(seq) - 1)
            return rseq

        reversedStr = reverseSequence(dfsStr)
        h2 = Hashing(reversedStr, base, mod)

        def isEven(num: int) -> bool:
            return (num % 2) == 0

        def processIndex(idx: int, acc: List[bool]) -> List[bool]:
            if idx == n:
                return acc
            lBound, rBound = pos[idx]
            lengthSub = rBound - lBound + 1
            halfLen = lengthSub // 2

            if isEven(lengthSub):
                val1 = h1.query(lBound, lBound + halfLen - 1)
                val2 = h2.query(n - rBound + 1, n - rBound + halfLen)
            else:
                val1 = h1.query(lBound, lBound + halfLen - 1)
                val2 = h2.query(n - rBound + 1, n - rBound + halfLen)

            acc.append(val1 == val2)
            return processIndex(idx + 1, acc)

        answerList = []
        return processIndex(0, answerList)