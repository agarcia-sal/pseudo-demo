class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            accumulator = 0
            counter = 0
            position = 0
            length = len(s)
            while position < length:
                counter += 1
                if position == length - 1 or s[position] != s[position + 1]:
                    accumulator += (counter // m) + 1
                    if accumulator > numOps:
                        return False
                    counter = 0
                position += 1
            return accumulator <= numOps

        totalLength = len(s)
        lowerBound = 1
        upperBound = totalLength
        while lowerBound < upperBound:
            midpoint = lowerBound + (upperBound - lowerBound) // 2
            if check(midpoint):
                upperBound = midpoint
            else:
                lowerBound = midpoint + 1
        return lowerBound