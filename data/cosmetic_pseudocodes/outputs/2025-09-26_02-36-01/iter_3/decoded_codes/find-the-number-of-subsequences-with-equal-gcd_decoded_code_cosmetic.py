class Solution:
    def subsequencePairCount(self, nums):
        modulus = 10**9 + 7
        upperBound = float('-inf')
        for val in nums:
            if val > upperBound:
                upperBound = val

        # Initialize table as (upperBound + 1) x (upperBound + 1) matrix of zeros
        table = [[0] * (upperBound + 1) for _ in range(upperBound + 1)]
        table[0][0] = 1

        for current in nums:
            nextTable = [[0] * (upperBound + 1) for _ in range(upperBound + 1)]
            for a in range(upperBound + 1):
                for b in range(upperBound + 1):
                    # add subsequences that exclude current element
                    nextTable[a][b] += table[a][b]
                    nextTable[a][b] %= modulus

                    # compute gcd of a and current
                    gcdA = a
                    divisorA = current
                    while divisorA != 0:
                        temp = divisorA
                        divisorA = gcdA % divisorA
                        gcdA = temp
                    newA = gcdA

                    # add subsequences that include current element in first subsequence gcd
                    nextTable[newA][b] += table[a][b]
                    nextTable[newA][b] %= modulus

                    # compute gcd of b and current
                    gcdB = b
                    divisorB = current
                    while divisorB != 0:
                        tmp = divisorB
                        divisorB = gcdB % divisorB
                        gcdB = tmp
                    newB = gcdB

                    # add subsequences that include current element in second subsequence gcd
                    nextTable[a][newB] += table[a][b]
                    nextTable[a][newB] %= modulus

            table = nextTable

        aggregate = 0
        for counter in range(1, upperBound + 1):
            aggregate += table[counter][counter]
        finalAnswer = aggregate % modulus
        return finalAnswer