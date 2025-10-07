class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        def computeHamming(binA: str, binB: str) -> int:
            cnt = 0
            idx = 0
            while idx < len(binA):
                if binA[idx] != binB[idx]:
                    cnt += 1
                idx += 1
            return cnt

        def toBinaryString(x: int, length: int) -> str:
            def recConvert(val: int, acc: str) -> str:
                if val == 0:
                    return acc
                else:
                    bit_char = '1' if (val % 2) == 1 else '0'
                    return recConvert(val // 2, bit_char + acc)
            binStr = recConvert(x, "")
            pad_len = length - len(binStr)
            padStr = ""
            ctr = 0
            while True:
                if ctr >= pad_len:
                    break
                padStr += "0"
                ctr += 1
            return padStr + binStr

        transformedNums = []
        u = 0
        while True:
            if u >= len(nums):
                break
            binForm = toBinaryString(nums[u], m)
            transformedNums.append(binForm)
            u += 1

        resultList = []
        a1 = 0
        while True:
            if a1 >= len(nums):
                break

            currMax = 0
            a2 = 0
            while True:
                if a2 >= len(nums):
                    break
                if a1 != a2:
                    hd_val = computeHamming(transformedNums[a1], transformedNums[a2])
                    if hd_val > currMax:
                        currMax = hd_val
                a2 += 1

            resultList.append(currMax)
            a1 += 1

        return resultList