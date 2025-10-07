class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            m = 9
            while m >= 1:
                if m % k == 0:
                    return str(m)
                m -= 1
            return "0"

        def makeFull(value: int) -> int:
            s = str(value)
            if n % 2 == 0:
                t = s + s[::-1]
            else:
                t = s + s[-2::-1]  # reverse all but last char
            return int(t)

        limitValue = int("9" * ((n + 1) // 2))

        def decreaseAndCheck(num: int) -> str:
            if num <= 0:
                return "0"
            candidate = makeFull(num)
            if candidate % k == 0:
                return str(candidate)
            return decreaseAndCheck(num - 1)

        return decreaseAndCheck(limitValue)