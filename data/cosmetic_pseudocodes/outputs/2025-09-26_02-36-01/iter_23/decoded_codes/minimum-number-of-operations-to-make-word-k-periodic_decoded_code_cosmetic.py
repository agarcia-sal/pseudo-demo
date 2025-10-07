class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        substringsList = []
        lengthVar = len(word)

        def loopRecursion(startIdx: int):
            if startIdx >= lengthVar:
                return
            tempSubstring_chars = []

            def substrBuilder(counter: int):
                if counter > k - 1 or startIdx + counter >= lengthVar:
                    return
                tempSubstring_chars.append(word[startIdx + counter])
                substrBuilder(counter + 1)

            substrBuilder(0)
            substringsList.append("".join(tempSubstring_chars))
            loopRecursion(startIdx + k)

        loopRecursion(0)

        segmentFrequency = {}

        def frequencyCounter(i: int):
            if i >= len(substringsList):
                return
            segmentFrequency[substringsList[i]] = segmentFrequency.get(substringsList[i], 0) + 1
            frequencyCounter(i + 1)

        frequencyCounter(0)

        highestFrequency = 0
        for key in segmentFrequency:
            if highestFrequency <= segmentFrequency[key]:
                highestFrequency = segmentFrequency[key]

        totalSegments = len(substringsList)
        computedResult = totalSegments - highestFrequency
        return computedResult