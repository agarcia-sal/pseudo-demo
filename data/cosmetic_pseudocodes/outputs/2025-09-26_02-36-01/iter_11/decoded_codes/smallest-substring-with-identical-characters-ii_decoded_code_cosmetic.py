class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            quantity = 0
            counter = 0

            def incrementAndEvaluate() -> bool:
                nonlocal quantity, counter
                quantity += (counter // m) + 1
                if quantity > numOps:
                    return False
                counter = 0
                return True

            index = 0
            n = len(s)
            while index < n:
                counter += 1
                if index == n - 1 or s[index] != s[index + 1]:
                    if not incrementAndEvaluate():
                        return False
                index += 1
            return quantity <= numOps

        strLen = len(s)
        low, high = 1, strLen

        def midPoint(x: int, y: int) -> int:
            return x + ((y - x) // 2)

        while low < high:
            middle = midPoint(low, high)
            if check(middle):
                high = middle
            else:
                low = middle + 1

        return low