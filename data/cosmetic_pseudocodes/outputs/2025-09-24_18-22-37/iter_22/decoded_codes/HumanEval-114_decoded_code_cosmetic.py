from typing import List

def minSubArraySum(nums: List[int]) -> int:
    currentTotal = 0
    peakTotal = 0
    idx = 0
    while idx < len(nums):
        negValue = -nums[idx]
        currentTotal += negValue
        if currentTotal < 0:
            currentTotal = 0
        if currentTotal > peakTotal:
            peakTotal = currentTotal
        idx += 1
    if peakTotal == 0:
        maxNeg = -nums[0]
        pos = 1
        while pos < len(nums):
            candidate = -nums[pos]
            if candidate > maxNeg:
                maxNeg = candidate
            pos += 1
        peakTotal = maxNeg
    result = -peakTotal
    return result