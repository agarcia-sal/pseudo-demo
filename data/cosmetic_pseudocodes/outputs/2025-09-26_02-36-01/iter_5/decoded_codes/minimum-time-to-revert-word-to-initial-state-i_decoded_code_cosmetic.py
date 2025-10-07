class Solution:
    def minimumTimeToInitialState(self, alpha: int) -> int:
        word = alpha
        beta = len(word)
        gamma = 1

        def checkCondition(delta: int) -> bool:
            if delta * alpha >= beta:
                return True
            return word[delta * alpha : beta] == word[0 : beta - delta * alpha]

        def recursiveSearch(epsilon: int) -> int:
            if checkCondition(epsilon):
                return epsilon
            return recursiveSearch(epsilon + 1)

        result = recursiveSearch(gamma)
        return result