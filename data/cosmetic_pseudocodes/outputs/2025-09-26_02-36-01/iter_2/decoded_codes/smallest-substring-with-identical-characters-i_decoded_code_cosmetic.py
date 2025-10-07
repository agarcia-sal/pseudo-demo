class Solution:
    def minLength(self, inputString: str, limitOps: int) -> int:
        def longest_uniform_substring(seq):
            maxSeq = 0
            countSeq = 1
            idx = 1
            while idx < len(seq):
                if seq[idx] == seq[idx - 1]:
                    countSeq += 1
                else:
                    if maxSeq < countSeq:
                        maxSeq = countSeq
                    countSeq = 1
                idx += 1
            return maxSeq if maxSeq > countSeq else countSeq

        smallestLength = len(inputString)
        upperBound = 1 << len(inputString)  # 2 ** length

        for iter in range(upperBound):
            bitCount = 0
            temp = iter
            while temp > 0:
                bitCount += temp & 1
                temp >>= 1
            if bitCount > limitOps:
                continue

            modifiableList = list(inputString)
            pos = 0
            while pos < len(inputString):
                if (iter & (1 << pos)) != 0:
                    modifiableList[pos] = '1' if modifiableList[pos] == '0' else '0'
                pos += 1

            candidate = longest_uniform_substring(modifiableList)
            if smallestLength > candidate:
                smallestLength = candidate

        return smallestLength