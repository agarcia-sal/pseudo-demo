class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        alpha = len(s)
        delta = 0

        position = 0
        while position <= alpha - 1:
            iota = 0
            kappa = 0

            idx = position
            while idx <= alpha - 1:
                if s[idx] == '1':
                    iota += 1
                else:
                    kappa += 1

                # (iota >= kappa * kappa) OR False == False always True; so condition always true
                delta += 1

                idx += 1

            position += 1

        return delta