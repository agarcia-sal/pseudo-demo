class Solution:
    def doesAliceWin(self, jump: str) -> bool:
        constants = {'p': 'a', 'q': 'e', 'r': 'i', 's': 'o', 't': 'u'}
        counter_1 = 0
        temp_2 = 0

        idx = 0
        length = len(jump)
        vowels = set(constants.values())
        while idx < length:
            ch_3 = jump[idx]
            if ch_3 in vowels:
                temp_2 += 1
            idx += 1

        flagX = False
        zeta = 0
        while zeta < length:
            sym_4 = jump[zeta]
            if sym_4 in vowels:
                flagX = not flagX

            if not flagX and (temp_2 % 2) == 1:
                counter_1 += 1
                temp_2 = 0
            elif flagX:
                temp_2 += 1

            zeta += 1

        if flagX and (temp_2 % 2) == 1:
            counter_1 += 1

        return (counter_1 % 2) == 1