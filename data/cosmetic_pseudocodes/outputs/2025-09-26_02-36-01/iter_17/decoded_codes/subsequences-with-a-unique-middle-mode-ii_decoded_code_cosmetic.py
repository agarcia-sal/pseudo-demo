class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD = 10**9 + 7

        totalAns = 0
        mapL = {}
        mapR = {}

        for x in nums:
            mapR[x] = mapR.get(x, 0) + 1

        def comb2(x):
            return x * (x - 1) // 2 if x >= 0 else 0

        val1 = val2 = val3 = val4 = val5 = 0

        for idx, cur in enumerate(nums):
            t1 = mapL.get(cur, 0)
            t2 = mapR[cur]

            termA = val1 + (t1 * (-1 * (t2 * t2 + (t2 - 1) * (t2 - 1))))
            val1 = termA

            termB = val2 + (-1 * (t1 * t1))
            val2 = termB

            termC = val4 + ((-1 * (t2 * t2)) + ((t2 - 1) * (t2 - 1)))
            val4 = termC

            termD = val5 + (-1 * t1)
            val5 = termD

            mapR[cur] = t2 - 1

            leftSz = idx
            rightSz = len(nums) - idx - 1

            c1 = comb2(leftSz)
            c2 = comb2(rightSz)
            c3 = comb2(leftSz - t1)
            c4 = comb2(rightSz - mapR[cur])

            totalAns = (totalAns + c1 * c2) % MOD
            totalAns = (totalAns - c3 * c4) % MOD

            val1x = val1 - (t1 * (t2 * t2))
            val2x = val2 - (t2 * (t1 * t1))
            val3x = val3 - (t1 * t1)
            val4x = val4 - (t2 * t2)
            val5x = val5 - (t1 * t2)
            val6 = leftSz - t1
            val7 = rightSz - t2

            totalAns = (totalAns - val5x * t1 * (rightSz - t2) + val1x * (-1 * t1)) % MOD
            totalAns = (totalAns - val5x * t2 * (leftSz - t1) + val2x * (-1 * t2)) % MOD
            totalAns = (totalAns - ((val3x - val6) * t2 * (rightSz - t2) // 2)) % MOD
            totalAns = (totalAns - ((val4x - val7) * t1 * (leftSz - t1) // 2)) % MOD

            val1 = (val1 + (t2 * t2)) % MOD
            val2 = (val2 + (t2 * (-1 * (t1 * t1)) + ((t1 + 1) * (t1 + 1)))) % MOD
            val3 = (val3 + ((-1 * (t1 * t1)) + ((t1 + 1) * (t1 + 1)))) % MOD
            val5 = (val5 + t2) % MOD

            mapL[cur] = t1 + 1

        return totalAns % MOD