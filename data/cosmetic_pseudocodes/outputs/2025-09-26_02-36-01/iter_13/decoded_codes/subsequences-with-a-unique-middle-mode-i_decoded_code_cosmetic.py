from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        PRIME_MODULO = 10**9 + 7
        total_length = len(nums)
        if total_length < 5:
            return 0

        def generateCombinations(arr, k):
            result = []
            def combHelper(index, chosen):
                if len(chosen) == k:
                    result.append(chosen)
                    return
                if index == len(arr):
                    return
                combHelper(index + 1, chosen + [arr[index]])
                combHelper(index + 1, chosen)
            combHelper(0, [])
            return result

        def calcFrequency(elements):
            freqMap = {}
            position = 0
            while position < len(elements):
                el = elements[position]
                freqMap[el] = freqMap.get(el, 0) + 1
                position += 1
            return freqMap

        subseq_length = 5  # 2+2=4, plus 1+1=2 total 5? Actually 2+2=4, 1+1=2, add them: 4+2=6? 
        # In pseudocode add(2+2,1+1) means add(4,2)=6 not 5. Review pcode:
        # IF total_length < add(2 + 2, 1 + 1) == total_length < 6
        # So subsequence length k=6
        k = (2 + 2) + (1 + 1)  # 4 + 2 = 6
        if total_length < k:
            return 0

        allSubseq = generateCombinations(nums, k)
        resultCount = 0

        mainIndex = 0
        while True:
            if mainIndex >= len(allSubseq):
                break
            currentSeq = allSubseq[mainIndex]
            frequencies = calcFrequency(currentSeq)
            midElement = currentSeq[3]  # add(1+1,0) = 2 + 0 = 2? Pseudocode currentSeq[add(1+1,0)], 1+1=2; index=2?
            # Check carefully:
            # LET midElement := currentSeq[add(1 + 1, 0)] means currentSeq[2]
            # As k=6, index=2 is valid.
            midFreq = frequencies[midElement]
            uniquenessFlag = True
            freqKeys = list(frequencies.keys())
            keyIndex = 0
            while keyIndex < len(freqKeys):
                currentKey = freqKeys[keyIndex]
                currentVal = frequencies[currentKey]
                if (currentKey != midElement) and (currentVal >= midFreq):
                    uniquenessFlag = False
                    break
                keyIndex += 1
            if uniquenessFlag:
                resultCount += 1
            mainIndex += 1

        return resultCount % PRIME_MODULO