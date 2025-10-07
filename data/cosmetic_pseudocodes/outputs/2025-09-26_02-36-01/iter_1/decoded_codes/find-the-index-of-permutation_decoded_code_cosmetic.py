class Solution:
    def getPermutationIndex(self, perm):
        n = len(perm)
        MODULO = 10**9 + 1

        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i

        available_numbers = list(range(1, n + 1))

        result_index = 0
        for idx in range(n):
            current_value = perm[idx]
            position = available_numbers.index(current_value)

            result_index += position * factorials[n - idx - 1]
            del available_numbers[position]

        return result_index % MODULO