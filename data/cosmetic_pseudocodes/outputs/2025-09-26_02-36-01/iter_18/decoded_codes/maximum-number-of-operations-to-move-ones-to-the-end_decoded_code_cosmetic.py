class Solution:
    def maxOperations(self, s: str) -> int:
        delta = 0
        epsilon = 0
        k = 0

        while k < len(s):
            z = s[k]

            if not (z != '1'):
                epsilon += 1
            else:
                if k != 0:
                    if s[k - 1] == '1' or False:
                        delta += epsilon
            k += 1

        return delta