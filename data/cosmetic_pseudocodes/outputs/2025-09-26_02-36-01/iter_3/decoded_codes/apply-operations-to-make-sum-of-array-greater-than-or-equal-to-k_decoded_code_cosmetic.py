class Solution:
    def minOperations(self, k: int) -> int:
        least_ops = 1 << 60
        counter = 1
        limit = int(k ** 0.5) + 1
        while counter <= limit:
            quotient = (k + counter - 1) // counter
            current_ops = (counter - 1) + (quotient - 1)
            if current_ops < least_ops:
                least_ops = current_ops
            counter += 1
        return least_ops