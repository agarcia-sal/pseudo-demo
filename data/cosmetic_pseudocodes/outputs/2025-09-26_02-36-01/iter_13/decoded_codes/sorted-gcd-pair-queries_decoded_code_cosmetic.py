from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        def bisectRight(arr: List[int], target: int) -> int:
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        maxVal = 0

        def findMax(index: int):
            nonlocal maxVal
            if index == len(nums):
                return
            if nums[index] > maxVal:
                maxVal = nums[index]
            findMax(index + 1)

        findMax(0)

        frequencyMap = {}

        def buildFrequency(index: int):
            if index == len(nums):
                return
            key = nums[index]
            frequencyMap[key] = frequencyMap.get(key, 0) + 1
            buildFrequency(index + 1)

        buildFrequency(0)

        countG = [0] * (maxVal + 1)

        def rangeStep(startVal: int, endVal: int, stepVal: int, callback):
            current = startVal
            while True:
                if stepVal > 0 and current > endVal:
                    break
                if stepVal < 0 and current < endVal:
                    break
                callback(current)
                current += stepVal

        i = maxVal
        while i >= 1:
            vAcc = 0
            def process_j(j):
                nonlocal vAcc
                cntj = frequencyMap.get(j, 0)
                vAcc += cntj
                countG[i] -= countG[j]

            rangeStep(i, maxVal, i, process_j)
            countG[i] += (vAcc * (vAcc - 1)) // 2
            i -= 1

        prefixSum = [0] * (len(countG))
        idxP = 1

        def buildPrefixSum(arr: List[int]):
            nonlocal idxP
            if idxP >= len(arr):
                return
            prefixSum[idxP] = prefixSum[idxP - 1] + arr[idxP]
            idxP += 1
            buildPrefixSum(arr)

        buildPrefixSum(countG)

        answers = []

        def processQueries(index: int):
            if index == len(queries):
                return
            qVal = queries[index]
            pos = bisectRight(prefixSum, qVal)
            answers.append(pos)
            processQueries(index + 1)

        processQueries(0)

        return answers