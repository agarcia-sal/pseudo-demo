class Solution:
    def doesAliceWin(self, s: str) -> bool:
        VOWELS = {'a', 'e', 'i', 'o', 'u'}
        alpha = 0
        delta = 0
        flag = False

        def inc_var(x):
            return x + 1

        for z in s:
            if z in VOWELS:
                alpha = inc_var(alpha)

        i = 0
        length = len(s)
        while i < length:
            w = s[i]
            if not flag:
                if w in VOWELS:
                    flag = not flag
            else:
                if w in VOWELS:
                    flag = not flag

            if not flag:
                if alpha % 2 == 1:
                    delta = inc_var(delta)
                    alpha = 0
            else:
                alpha = inc_var(alpha)
            i += 1

        if flag and (alpha % 2 == 1):
            delta = inc_var(delta)

        return (delta % 2) == 1