class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:

        def substrEqual(str_: str, start: int, pattern: str) -> bool:
            m = len(pattern)
            n = len(str_)
            if start < 0 or start > n - m:
                return False
            for idx in range(m):
                if str_[start + idx] != pattern[idx]:
                    return False
            return True

        def findIndices(str_: str, sub: str) -> list[int]:
            res = []
            pos = 0
            limit = len(str_) - len(sub)
            while pos <= limit:
                if substrEqual(str_, pos, sub):
                    res.append(pos)
                pos += 1
            return res

        collection_x = findIndices(s, a)
        collection_y = findIndices(s, b)
        resultIndices = []

        def walk(i: int, j: int):
            if i >= len(collection_x) or j >= len(collection_y):
                return
            diff = collection_x[i] - collection_y[j]
            if diff < 0:
                diff = -diff
            if diff <= k:
                resultIndices.append(collection_x[i])
                walk(i + 1, j)
            else:
                if collection_x[i] < collection_y[j]:
                    walk(i + 1, j)
                else:
                    walk(i, j + 1)

        walk(0, 0)
        return resultIndices