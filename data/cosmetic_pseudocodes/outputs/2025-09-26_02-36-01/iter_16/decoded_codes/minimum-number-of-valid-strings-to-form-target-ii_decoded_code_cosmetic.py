class Solution:
    def minValidStrings(self, words, target):
        alpha = set()
        m = 0
        while m < len(words):
            beta = words[m]
            x = 1
            while True:
                if x > len(beta):
                    break
                gamma = ""
                y = 0
                while y < x:
                    gamma += beta[y]
                    y += 1
                alpha.add(gamma)
                x += 1
            m += 1

        z = len(target)
        dp = [float('inf')] * (z + 1)
        dp[0] = 0
        i = 1
        while True:
            if i > z:
                break
            j = 1
            while j <= i:
                delta = ""
                for k in range(j - 1, i):
                    delta += target[k]
                if delta in alpha:
                    candidate = dp[j - 1] + 1
                    if dp[i] > candidate:
                        dp[i] = candidate
                j += 1
            i += 1

        return dp[z] if dp[z] != float('inf') else -1