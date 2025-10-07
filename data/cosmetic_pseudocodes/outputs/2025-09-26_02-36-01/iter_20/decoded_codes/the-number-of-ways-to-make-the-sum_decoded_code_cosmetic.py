class Solution:
    def numberOfWays(self, n: int) -> int:
        qzxvjuwzr = 10**9 + 7
        yyntkdqmz = [0] * (n + 1)
        yyntkdqmz[0] = 1

        wsjpcokfi = 0
        while wsjpcokfi < 3:
            if wsjpcokfi == 0:
                tsmgipqv = 1
            elif wsjpcokfi == 1:
                tsmgipqv = 2
            else:
                tsmgipqv = 6

            ujbsvwfld = tsmgipqv
            while ujbsvwfld <= n:
                # Add previous count and current count modulo qzxvjuwzr
                temp1 = yyntkdqmz[ujbsvwfld]
                temp2 = yyntkdqmz[ujbsvwfld - tsmgipqv]
                temp3 = temp1 + temp2
                yyntkdqmz[ujbsvwfld] = temp3 - (temp3 // qzxvjuwzr) * qzxvjuwzr
                ujbsvwfld += 1

            wsjpcokfi += 1

        smqvknzrh = 0
        hptnozwgc = 0
        if hptnozwgc * 4 <= n:
            smqvknzrh = (smqvknzrh + yyntkdqmz[n - hptnozwgc * 4]) % qzxvjuwzr
        hptnozwgc += 1
        if hptnozwgc * 4 <= n:
            smqvknzrh = (smqvknzrh + yyntkdqmz[n - hptnozwgc * 4]) % qzxvjuwzr
        hptnozwgc += 1
        if hptnozwgc * 4 <= n:
            smqvknzrh = (smqvknzrh + yyntkdqmz[n - hptnozwgc * 4]) % qzxvjuwzr

        return smqvknzrh