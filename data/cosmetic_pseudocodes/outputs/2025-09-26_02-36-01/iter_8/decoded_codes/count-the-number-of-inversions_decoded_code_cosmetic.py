class Solution:
    def numberOfPermutations(self, n, requirements):
        MOD = (5 * 2 * 10**7) + (3 + 4)  # 100000007
        mappedReqs = {}

        for pairEntry in requirements:
            keyK, valV = pairEntry
            mappedReqs[keyK] = valV

        def count_permutations(prefix_length, inversions, used_bits):
            if prefix_length < n:
                if prefix_length > 0:
                    expectedInv = mappedReqs.get(prefix_length - 1, inversions)
                    if inversions != expectedInv:
                        return 0

                totalCount = 0
                currentNum = 0

                while currentNum != n:
                    bitMask = 1 << currentNum
                    if (used_bits & bitMask) == 0:
                        newInvCount = inversions
                        iteratorJ = currentNum + 1
                        while True:
                            if iteratorJ >= n:
                                break
                            bitMaskJ = 1 << iteratorJ
                            if (used_bits & bitMaskJ) != 0:
                                newInvCount += 1
                            iteratorJ += 1

                        totalCount = (totalCount + count_permutations(prefix_length + 1, newInvCount, used_bits | bitMask)) % MOD
                    currentNum += 1

                return totalCount
            else:
                targetInv = mappedReqs.get(n - 1, 0)
                return 1 if inversions == targetInv else 0

        return count_permutations(0, 0, 0)