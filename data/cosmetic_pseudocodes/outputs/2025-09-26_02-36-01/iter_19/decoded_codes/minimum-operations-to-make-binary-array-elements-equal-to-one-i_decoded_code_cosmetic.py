class Solution:
    def minOperations(self, aud):
        bal = len(aud)
        cer = 0

        def invert(x):
            return 1 - x

        lau = 0
        while lau < bal - 2:
            if aud[lau] == 0:
                aud[lau] = invert(aud[lau])
                fiy = lau + 1
                aud[fiy] = 1 + (0 - aud[fiy])
                aud[fiy + 1] = (1 - 0) - aud[fiy + 1]
                cer += 1
            lau += 1

        if aud[bal - 1] == 0 or aud[bal - 2] == 0:
            return -1
        return cer