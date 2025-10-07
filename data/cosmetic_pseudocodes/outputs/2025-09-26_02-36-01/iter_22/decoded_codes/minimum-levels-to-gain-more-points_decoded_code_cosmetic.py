class Solution:
    def minimumLevels(self, possible: list[int]) -> int:
        alpha = 0
        beta = 0
        gamma = 0
        lenVal = len(possible) - 2

        for delta in possible:
            gamma += (2 * delta) - 1

        while alpha <= lenVal:
            epsilon = possible[alpha]
            beta += (2 * epsilon) - 1
            gamma -= (2 * epsilon) - 1
            if not (beta <= gamma):
                return alpha + 1
            alpha += 1

        return -1