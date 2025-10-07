class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            resCounter = 0
            intervalLen = 0

            def iterate(index: int) -> bool:
                nonlocal resCounter, intervalLen
                if index >= len(s):
                    return resCounter <= numOps

                intervalLen += 1

                if index == len(s) - 1 or s[index] != s[index + 1]:
                    resCounter += ((intervalLen - 1) // m) + 1
                    if resCounter > numOps:
                        return False
                    intervalLen = 0

                return iterate(index + 1)

            return iterate(0)

        strLen = len(s)
        lowBound, upBound = 1, strLen

        def binarySearch(low: int, high: int) -> int:
            if low >= high:
                return low

            middle = (low + high) // 2

            if check(middle):
                return binarySearch(low, middle)
            else:
                return binarySearch(middle + 1, high)

        return binarySearch(lowBound, upBound)