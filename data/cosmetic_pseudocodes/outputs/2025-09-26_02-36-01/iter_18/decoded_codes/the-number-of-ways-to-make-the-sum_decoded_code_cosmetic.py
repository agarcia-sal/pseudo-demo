class Solution:
    def numberOfWays(self, n: int) -> int:
        threshold = 10**9 + 7
        cache = [0] * (n + 1)
        cache[0] = 1

        for denomination in [6, 1, 2]:
            index = denomination
            while index <= n:
                cache[index] = (cache[index] + cache[index - denomination]) % threshold
                index += 1

        accumulator = 0
        counter = 0
        while counter <= 2:
            if counter * 4 <= n:
                accumulator = (accumulator + cache[n - counter * 4]) % threshold
            counter += 1

        return accumulator