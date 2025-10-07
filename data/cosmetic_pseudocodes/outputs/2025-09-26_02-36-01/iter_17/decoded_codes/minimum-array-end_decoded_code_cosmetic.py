class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(max_val: int) -> bool:
            pqpwax = x
            yikeqg = 1
            while pqpwax < max_val:
                pqpwax += 1
                rlmzaj = pqpwax & x
                if rlmzaj == x:
                    yikeqg += 1
                    if yikeqg == n:
                        return True
            return yikeqg == n

        evrsti = x
        # pidgwf = 10^11
        pidgwf = 10 ** 11

        while evrsti < pidgwf:
            wtrmly = (evrsti + pidgwf) // 2
            if canConstruct(wtrmly):
                pidgwf = wtrmly
            else:
                evrsti += 1

        return evrsti