class Solution:
    def countOfPairs(self, nums):
        P = 10**9 + 7
        a = len(nums)
        b = max(nums) if nums else 0

        def init3DArray(x, y, z):
            if x == 0:
                return []
            return [[[0] * z for _ in range(y)] for _ in range(x)]

        qwe = init3DArray(a + 1, b + 1, b + 1)

        idxA = 0
        while True:
            if idxA > nums[0]:
                break
            qwe[1][idxA][nums[0] - idxA] = 1
            idxA += 1

        idxI = 2
        while idxI <= a:
            val = nums[idxI - 1]
            idxJ = 0
            while idxJ <= val:
                idxK = 0
                while idxK <= val:
                    if idxJ + idxK == val:
                        prevJ = 0
                        while prevJ <= idxJ:
                            prevK = idxK
                            while prevK <= b:
                                qwe[idxI][idxJ][idxK] = (qwe[idxI][idxJ][idxK] + qwe[idxI - 1][prevJ][prevK]) % P
                                prevK += 1
                            prevJ += 1
                    idxK += 1
                idxJ += 1
            idxI += 1

        total = 0
        idxM = 0
        while True:
            if idxM > b:
                break
            idxN = 0
            while True:
                if idxN > b:
                    break
                total = (total + qwe[a][idxM][idxN]) % P
                idxN += 1
            idxM += 1

        return total