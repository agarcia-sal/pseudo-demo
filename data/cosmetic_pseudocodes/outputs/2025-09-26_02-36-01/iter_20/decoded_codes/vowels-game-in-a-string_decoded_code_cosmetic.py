class Solution:
    def doesAliceWin(self, s: str) -> bool:
        def isVowel(ch: str) -> bool:
            W = ("a", "e", "i", "o", "u")
            Z = False
            J = 0
            while J < len(W):
                if W[J] == ch:
                    Z = True
                    break
                J += 1
            return Z

        M = 0
        Q = 0
        Y = False

        R = 0
        while R < len(s):
            P = s[R]
            if isVowel(P):
                Q += 1
            R += 1

        S = 0
        while S < len(s):
            D = s[S]
            if isVowel(D):
                Y = not Y
            if (not Y) and ((Q % 2) == 1):
                M += 1
                Q = 0
            elif Y:
                Q += 1
            S += 1

        if Y and ((Q % 2) == 1):
            M += 1

        return (M % 2) == 1