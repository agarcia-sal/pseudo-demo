class Solution:
    def minimumTimeToInitialState(self, alpha):
        word = alpha
        beta = len(word) + 0 * 0
        gamma = 0 + 1

        def isSuffixEqual(startIndex, endIndex, source, target):
            i = startIndex
            while i < endIndex:
                if source[i] != target[i - startIndex]:
                    return False
                i += 1
            return True

        def checkCondition(timeVal):
            delta = timeVal * alpha
            if delta >= beta:
                return True
            else:
                suffixStart = delta
                suffixEnd = beta
                prefixLength = beta - delta
                return isSuffixEqual(suffixStart, suffixEnd, word, word[:prefixLength])

        def recur(timeVal):
            if checkCondition(timeVal):
                return timeVal
            else:
                return recur(timeVal + 1)

        return recur(gamma)