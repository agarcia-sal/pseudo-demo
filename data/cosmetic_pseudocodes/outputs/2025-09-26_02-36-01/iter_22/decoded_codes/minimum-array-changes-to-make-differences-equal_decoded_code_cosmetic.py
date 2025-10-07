class Solution:
    def minChanges(self, nums, k):
        totalLen = len(nums)
        halfLen = (totalLen // 2) - 1
        arrD = [0] * (k + 2)
        idxP = 0
        while idxP <= halfLen:
            valL = nums[idxP]
            valR = nums[totalLen - idxP - 1]
            if valL > valR:
                valA, valB = valR, valL
            else:
                valA, valB = valL, valR

            arrD[0] += 1
            arrD[valB - valA] -= 1
            arrD[valB - valA + 1] += 1
            maxVal = valB
            tempSum = k - valA + 1
            idx1 = maxVal + tempSum
            if idx1 < len(arrD):
                arrD[idx1] -= 1
            idx2 = maxVal + tempSum + 1
            if idx2 < len(arrD):
                arrD[idx2] += 1
            idxP += 1

        accum = 0
        resultMin = float('inf')
        for val in arrD:
            accum += val
            if accum < resultMin:
                resultMin = accum
        return resultMin