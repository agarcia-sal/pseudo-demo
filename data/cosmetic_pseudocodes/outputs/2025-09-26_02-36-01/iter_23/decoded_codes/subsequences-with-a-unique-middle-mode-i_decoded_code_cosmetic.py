class Solution:
    def subsequencesWithMiddleMode(self, nums):
        M = 10**9 + 7
        length = len(nums)
        if length < 5:
            return 0

        def generateCombs(arr, k):
            result = []

            def rec(startIdx, path):
                if len(path) == k:
                    result.append(path)
                    return
                if startIdx >= len(arr):
                    return
                rec(startIdx + 1, path + [arr[startIdx]])
                rec(startIdx + 1, path)

            rec(0, [])
            return result

        subs = generateCombs(nums, 5)

        def countFreq(lst):
            freq = {}
            for elem in lst:
                freq[elem] = freq.get(elem, 0) + 1
            return freq

        def anyViolation(freqMap, midElem, midCnt):
            for key, val in freqMap.items():
                if key != midElem and val >= midCnt:
                    return True
            return False

        def processSubs(idx, acc):
            if idx == len(subs):
                return acc
            currentSub = subs[idx]
            frequencies = countFreq(currentSub)
            mElem = currentSub[2]
            mCount = frequencies[mElem]
            flag = not anyViolation(frequencies, mElem, mCount)
            if flag:
                return processSubs(idx + 1, acc + 1)
            else:
                return processSubs(idx + 1, acc)

        return processSubs(0, 0) % M