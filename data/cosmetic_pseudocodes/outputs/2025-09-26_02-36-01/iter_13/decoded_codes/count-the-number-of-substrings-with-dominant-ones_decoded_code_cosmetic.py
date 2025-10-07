class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        totalLength = len(s)
        aggregateCount = 0

        class RefCount:
            def __init__(self):
                self.value = 0

        def ProcessEndPosition(pos, oneCount, zeroCount, incrementCountRef):
            if pos >= totalLength:
                return
            currentChar = s[pos]
            if currentChar == '1':
                updatedOneCount = oneCount + 1
                updatedZeroCount = zeroCount
            else:
                updatedOneCount = oneCount
                updatedZeroCount = zeroCount + 1

            if updatedOneCount >= updatedZeroCount * updatedZeroCount:
                incrementCountRef.value += 1

            ProcessEndPosition(pos + 1, updatedOneCount, updatedZeroCount, incrementCountRef)

        pointer = 0
        while pointer < totalLength:
            counterRef = RefCount()
            ProcessEndPosition(pointer, 0, 0, counterRef)
            aggregateCount += counterRef.value
            pointer += 1

        return aggregateCount