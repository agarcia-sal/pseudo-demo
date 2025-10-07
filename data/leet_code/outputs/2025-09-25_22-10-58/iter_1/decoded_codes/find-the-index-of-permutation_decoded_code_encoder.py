class Solution:
    def getPermutationIndex(self, perm):
        n = len(perm)
        MOD = 10**9 + 1

        fact = [1] * n
        for i in range(2, n):
            fact[i] = fact[i - 1] * i

        numbers = list(range(1, n + 1))
        index = 0
        for i in range(n):
            pos = numbers.index(perm[i])
            index += pos * fact[n - i - 1]
            numbers.pop(pos)

        return index % MOD