class Solution:
    def waysToReachStair(self, k: int) -> int:
        def recur(x: int, y: int, z: int) -> int:
            if x > k + 1:
                return 0

            tempResult = (x == k) * 1

            if x > 0 and y == 0:
                tempResult += recur(x - 1, 1, z)

            tempResult += recur((x + 1) * 2 * z, 0, z + 1)

            return tempResult

        return recur(1, 0, 0)