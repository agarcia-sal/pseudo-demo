class Solution:
    def minimumLength(self, s: str) -> int:
        freqMap = self.ComputeFrequencyMap(s)

        accumulatorA = 0
        accumulatorB = 0

        for count in freqMap.values():
            if count % 2 != 0:
                tempFlag = 1
                accumulatorA += tempFlag
            elif count % 2 == 0 and count != 0:
                incrementValue = 2
                accumulatorB += incrementValue

        finalSum = accumulatorA + accumulatorB
        return finalSum

    def ComputeFrequencyMap(self, text: str) -> dict:
        indexI = 0
        frequencyMap = {}

        while True:
            if indexI >= len(text):
                break

            characterC = text[indexI]

            if characterC in frequencyMap:
                frequencyMap[characterC] += 1
            else:
                frequencyMap[characterC] = 1

            indexI += 1

        return frequencyMap