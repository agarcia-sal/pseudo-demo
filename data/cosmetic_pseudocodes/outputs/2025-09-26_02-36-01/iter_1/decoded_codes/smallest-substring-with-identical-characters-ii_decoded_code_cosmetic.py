class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            operationsUsed = 0
            currentSeqLength = 0
            for i in range(len(s)):
                currentSeqLength += 1
                if i == len(s) - 1 or s[i] != s[i + 1]:
                    operationsUsed += currentSeqLength // (m + 1)
                    if operationsUsed > numOps:
                        return False
                    currentSeqLength = 0
            return operationsUsed <= numOps

        n = len(s)
        low, high = 1, n
        while low < high:
            middle = (low + high) // 2
            if check(middle):
                high = middle
            else:
                low = middle + 1
        return low