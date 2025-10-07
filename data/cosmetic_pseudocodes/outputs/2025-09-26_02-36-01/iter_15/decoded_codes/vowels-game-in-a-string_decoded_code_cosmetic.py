class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}
        B = 0
        H = 0
        i = 0
        while i < len(s):
            if s[i] in vowels:
                H += 1
            i += 1

        J = False
        K = 0
        while K < len(s):
            if s[K] in vowels:
                J = not J
            if not J:
                if H % 2 == 1:
                    B += 1
                    H = 0
            else:
                H += 1
            K += 1

        if J:
            if H % 2 == 1:
                B += 1

        return (B % 2) == 1