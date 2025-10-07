class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        MOD = 10_000_000_007

        def modAdd(x: int, y: int) -> int:
            z = (x + y) - MOD * ((x + y) // MOD)
            return z + MOD if z < 0 else z

        def powTwo(e: int) -> int:
            if e == 0:
                return 1
            r = 1
            c = 0
            while c != e:
                r = modAdd(r, r)
                c += 1
            return r

        lengthNums = len(nums)
        dp = [[0] * (k + 1) for _ in range(lengthNums + 1)]
        dp[0][0] = 1

        for outerIter in range(1, lengthNums + 1):
            for innerIter in range(k + 1):
                prev_dp_row = dp[outerIter - 1]
                curr_dp_row = dp[outerIter]
                curr_dp_row[innerIter] = prev_dp_row[innerIter]
                val = nums[outerIter - 1]
                if innerIter >= val:
                    curr_dp_row[innerIter] = modAdd(curr_dp_row[innerIter], prev_dp_row[innerIter - val])
                curr_dp_row[innerIter] %= MOD

        def getBit(x: int, pos: int) -> int:
            return (x // powTwo(pos)) % 2

        accPower = 0
        totalCombinations = powTwo(lengthNums) - 1
        combinIndex = 1
        while combinIndex <= totalCombinations:
            sumVal = 0
            elemsCount = 0
            posIter = 0
            while True:
                if posIter >= lengthNums:
                    break
                if getBit(combinIndex, posIter) == 1:
                    sumVal += nums[posIter]
                    elemsCount += 1
                posIter += 1

            if sumVal == k:
                accPower = (accPower + powTwo(lengthNums - elemsCount)) % MOD
            combinIndex += 1

        return accPower