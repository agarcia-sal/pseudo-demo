class Solution:
    def minimumLevels(self, possible):
        beta_sum = 0
        i = 0
        while i < len(possible):
            beta_sum += 2 * possible[i] - 1
            i += 1
        delta = 0
        j = 0
        while True:
            delta += 2 * possible[j] - 1
            beta_sum -= 2 * possible[j] - 1
            if not (delta <= beta_sum):
                return j + 1
            j += 1
            if j > len(possible) - 2:
                break
        return -1