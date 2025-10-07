class Solution:
    def minLength(self, s: str, numOps: int) -> int:

        def check(m: int) -> bool:
            accumulator = 0
            tracker = 0
            check_over = False
            n = len(s)

            def exceedsLimit(value: int, limit: int) -> bool:
                return value > limit

            def conditionTrue(i: int, length: int, currChar: str, nextChar: str) -> bool:
                if i == length - 1:
                    return True
                else:
                    return currChar != nextChar

            def integerDivide(dividend: int, divisor: int) -> int:
                return (dividend - (dividend % divisor)) // divisor

            def iteratePosition(pos: int) -> None:
                nonlocal accumulator, tracker, check_over
                tracker += 1
                if conditionTrue(pos, n, s[pos], s[pos + 1] if pos + 1 < n else ''):
                    accumulator += integerDivide(tracker, m) + 1
                    if exceedsLimit(accumulator, numOps):
                        check_over = True
                    tracker = 0

            def repeatCheck(currentIndex: int) -> None:
                if currentIndex >= n:
                    return
                iteratePosition(currentIndex)
                if not check_over:
                    repeatCheck(currentIndex + 1)

            repeatCheck(0)

            if check_over:
                return False
            return accumulator <= numOps

        def integerHalf(value: int) -> int:
            return (value - (value % 2)) // 2

        def binarySearchRange(minimum: int, maximum: int) -> int:
            left, right = minimum, maximum
            result = maximum
            while left < right:
                midpoint = left + integerHalf(right - left)
                if check(midpoint):
                    right = midpoint
                    result = midpoint
                else:
                    left = midpoint + 1
            return result

        lengthOfString = len(s)
        start = 1
        end = lengthOfString

        answer = binarySearchRange(start, end)

        return answer