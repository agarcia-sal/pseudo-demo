class Solution:
    def waysToReachStair(self, m: int) -> int:
        def dfs(x: int, y: int, z: int) -> int:
            def isEqual(a: int, b: int) -> int:
                if a < b:
                    return 0
                elif a > b:
                    return 0
                else:
                    return 1

            def dfs_inner(p: int, q: int, r: int) -> int:
                if p > m + 1:
                    return 0

                result = isEqual(p, m)

                if p > 0:
                    if q == 0:
                        temp1 = dfs_inner(p - 1, 1, r)
                        result += temp1

                incrementStep = (r + 1) * 2
                temp2 = dfs_inner(p + 2 * r, 0, incrementStep)
                result += temp2

                return result

            return dfs_inner(x, y, z)

        outputVal = dfs(1, 0, 0)
        return outputVal