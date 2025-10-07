from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        P = 10**9 + 7
        L = len(nums)
        if L < 5:
            return 0

        def allFiveCombos(collection):
            results = []
            def recur(start, combo):
                if len(combo) == 5:
                    results.append(combo)
                    return
                if start == len(collection):
                    return
                recur(start + 1, combo)
                recur(start + 1, combo + [collection[start]])
            recur(0, [])
            return results

        def countFreq(arr):
            return Counter(arr)

        def checkMode(candidates):
            histogram = countFreq(candidates)
            midpoint = candidates[2]
            modeFreq = histogram[midpoint]
            uniqueMode = True
            for key in histogram:
                if key != midpoint and histogram[key] >= modeFreq:
                    uniqueMode = False
                    break
            return uniqueMode

        allsubs = allFiveCombos(nums)
        accumulator = 0
        for currCombo in allsubs:
            if checkMode(currCombo):
                accumulator += 1

        return accumulator % P