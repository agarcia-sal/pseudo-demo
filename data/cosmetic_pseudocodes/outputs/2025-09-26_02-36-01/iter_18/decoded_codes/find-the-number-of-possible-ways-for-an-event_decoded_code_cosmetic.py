class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        constantLimit = 10**9 + 7
        matrixVar = [[0] * (x + 1) for _ in range(n + 1)]
        matrixVar[0][0] = 1

        for alpha in range(1, n + 1):
            for beta in range(1, x + 1):
                firstTerm = matrixVar[alpha - 1][beta] * beta
                secondTerm = matrixVar[alpha - 1][beta - 1] * (x - (beta - 1))
                combinedSum = firstTerm + secondTerm
                matrixVar[alpha][beta] = combinedSum % constantLimit

        aggregateResult = 0
        progressivePower = 1
        counterVar = 1
        while counterVar <= x:
            progressivePower = (progressivePower * y) % constantLimit
            contributionValue = matrixVar[n][counterVar] * progressivePower
            aggregateResult = (aggregateResult + contributionValue) % constantLimit
            counterVar += 1

        return aggregateResult