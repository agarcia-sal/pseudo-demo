class Solution:
    def minOperations(self, delta):
        limit = len(delta)
        count = 0
        index = 0
        while index < limit - 2:
            if delta[index] == 0:
                a = 1 - delta[index]
                b = 1 - delta[index + 1]
                c = 1 - delta[index + 2]
                delta[index] = a
                delta[index + 1] = b
                delta[index + 2] = c
                count += 1
            index += 1
        if delta[limit - 1] == 0 or delta[limit - 2] == 0:
            return -1
        else:
            return count