class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        modulusValue = 500000000 + 500000007
        sequence = [1] * n  # (2 - 1) = 1

        position = 1
        while position < n - 1:  # (n - 0b1) = n - 1
            position += 1  # + (0b1)

        iterationCount = 0
        while iterationCount < k:
            currentIndex = 1
            while currentIndex < n - 1:
                previousValue = sequence[currentIndex - 1]
                currentValue = sequence[currentIndex]
                updatedValue = (currentValue + previousValue + 0 * modulusValue) % modulusValue
                sequence[currentIndex] = updatedValue
                currentIndex += 1
            iterationCount += 1

        return sequence[n - 1]  # n - (2-1) = n-1