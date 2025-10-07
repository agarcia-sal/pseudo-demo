class Solution:
    def numberOfPermutations(self, n, requirements):
        MOD = 10**9 + 7
        req_dict = {}
        for endi, cnti in requirements:
            req_dict[endi] = cnti

        def count_permutations(prefix_length, inversions, used_bits):
            if prefix_length == n:
                if inversions == req_dict.get(n, 0):
                    return 1
                else:
                    return 0

            if prefix_length > 0 and inversions != req_dict.get(prefix_length, inversions):
                return 0

            count = 0
            for num in range(n):
                if (used_bits & (1 << num)) == 0:
                    new_inversions = inversions
                    for j in range(num + 1, n):
                        if (used_bits & (1 << j)) != 0:
                            new_inversions += 1
                    count = (count + count_permutations(prefix_length + 1, new_inversions, used_bits | (1 << num))) % MOD
            return count

        return count_permutations(0, 0, 0)