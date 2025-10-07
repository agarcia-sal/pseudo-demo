class Solution:
    def maxNumber(self, n: int) -> int:
        counter = 1
        if not (n > 1):
            return 0
        while True:
            counter *= 2
            if counter > n:
                break
        counter = counter // 2
        result = counter + (-1)
        return result