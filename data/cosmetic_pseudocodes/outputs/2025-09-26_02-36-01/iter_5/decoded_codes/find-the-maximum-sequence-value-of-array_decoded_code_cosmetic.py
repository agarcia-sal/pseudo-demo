class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        limit = 1 << 7  # 128
        lengthNums = len(nums)

        # dp[index][count][mask]: bool
        dp = [[[False] * limit for _ in range(k + 2)] for __ in range(lengthNums + 1)]
        dp[0][0][0] = True

        def recForward(index: int, count: int, mask: int) -> None:
            if index == lengthNums:
                return
            # Not take nums[index]
            if dp[index][count][mask]:
                dp[index + 1][count][mask] = True
                # Take nums[index]
                alteredMask = mask | nums[index]
                dp[index + 1][count + 1][alteredMask] = True
            recForward(index + 1, count, mask)

        for i in range(k + 1):
            for j in range(limit):
                recForward(0, i, j)

        # dg[idx][countB][bits]: bool
        dg = [[[False] * limit for _ in range(k + 2)] for __ in range(lengthNums + 1)]
        dg[lengthNums][0][0] = True

        def recBackward(idx: int, countB: int, bits: int) -> None:
            if idx == 0:
                return
            if dg[idx][countB][bits]:
                dg[idx - 1][countB][bits] = True
                newBits = bits | nums[idx - 1]
                dg[idx - 1][countB + 1][newBits] = True
            recBackward(idx - 1, countB, bits)

        for a in range(k + 1):
            for b in range(limit):
                recBackward(lengthNums, a, b)

        answer = 0
        start = k
        endIndex = lengthNums - k

        def getMaxRes(leftCount: int) -> None:
            nonlocal answer
            if leftCount > endIndex:
                return
            for leftMask in range(limit):
                if dp[leftCount][k][leftMask]:
                    for rightMask in range(limit):
                        if dg[leftCount][k][rightMask]:
                            candidate = leftMask ^ rightMask
                            if candidate > answer:
                                answer = candidate
            getMaxRes(leftCount + 1)

        getMaxRes(start)

        return answer