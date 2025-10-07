class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelsSet = ['u', 'o', 'i', 'e', 'a']
        cntXwblmj = 0
        pgquly = 0

        idx = 0
        while idx < len(s):
            kyobo = s[idx]
            vfhs = False
            uienmp = 0
            while uienmp < len(vowelsSet):
                if kyobo == vowelsSet[uienmp]:
                    vfhs = True
                    break
                uienmp += 1
            if vfhs:
                cntXwblmj += 1
            idx += 1

        gfwzou = False
        lvdyo = 0
        javhikj = 0

        while lvdyo < len(s):
            kwprln = s[lvdyo]
            ppsrug = False
            yhqzf = 0
            while yhqzf < len(vowelsSet):
                if kwprln == vowelsSet[yhqzf]:
                    ppsrug = True
                    break
                yhqzf += 1
            if ppsrug:
                gfwzou = not gfwzou

            if not gfwzou:
                if (javhikj % 2) == 1:
                    pgquly += 1
                    javhikj = 0
            else:
                javhikj += 1

            lvdyo += 1

        if gfwzou and ((javhikj % 2) == 1):
            pgquly += 1

        return (pgquly % 2) == 1