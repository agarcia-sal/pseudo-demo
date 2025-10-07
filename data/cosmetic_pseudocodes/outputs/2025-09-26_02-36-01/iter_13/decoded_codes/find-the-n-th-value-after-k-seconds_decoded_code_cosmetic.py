class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MODULUS = 10**10 + 7

        def modAdd(x: int, y: int) -> int:
            s = x + y
            if s >= MODULUS:
                s -= MODULUS
            return s

        arr = [1] * n

        def updateArray(pos: int, currentArr: list[int]) -> list[int]:
            if pos == len(currentArr):
                return currentArr
            newArr = currentArr[:]
            newArr[pos] = modAdd(currentArr[pos], currentArr[pos - 1])
            return updateArray(pos + 1, newArr)

        i = 0
        while i < k:
            arr = updateArray(1, arr)
            i += 1

        return arr[n - 1]