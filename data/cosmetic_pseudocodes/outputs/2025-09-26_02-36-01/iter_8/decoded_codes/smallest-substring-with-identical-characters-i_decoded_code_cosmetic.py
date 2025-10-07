class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def longest_uniform_substring(s_list):
            longestSeq = 0
            seqCount = 1
            idx = 1
            length = len(s_list)
            while idx < length:
                if s_list[idx] == s_list[idx - 1]:
                    seqCount += 1
                else:
                    if longestSeq < seqCount:
                        longestSeq = seqCount
                    seqCount = 1
                idx += 1
            return max(longestSeq, seqCount)

        finalMin = len(s)
        upperBound = 1 << len(s)
        iterIndex = 0
        while iterIndex < upperBound:
            if bin(iterIndex).count('1') > numOps:
                iterIndex += 1
                continue

            tempList = list(s)

            for posCounter in range(len(s)):
                flagBit = 1 << posCounter
                if (iterIndex & flagBit) != 0:
                    tempList[posCounter] = '1' if tempList[posCounter] == '0' else '0'

            currentCandidate = longest_uniform_substring(tempList)
            if finalMin > currentCandidate:
                finalMin = currentCandidate
            iterIndex += 1

        return finalMin