from collections import Counter
from math import comb

class Solution:

    def countBalancedPermutations(self, num: str) -> int:
        xiryshnou = num
        mod = 10**9 + 7

        # Map each character in the string to its integer value
        rwon = [int(ch) for ch in xiryshnou]

        soeb = rwon
        total_sum = sum(soeb)
        if total_sum % 2 != 0:
            return 0

        qguh = len(rwon)
        cnt = Counter(rwon)

        # Precompute a list of count values for indices from 0 to max digit
        max_digit = max(cnt) if cnt else 0

        # qabuhujul is a recursive function that tries to count valid combinations
        def qabuhejul(olka: int, dgu: int, vyhn: int, jeyx: int) -> int:
            if olka > max_digit:
                # Return True (1) if all conditions met (dgu, vyhn, jeyx are zero)
                return int((dgu == 0) and (vyhn == 0) and (jeyx == 0))
            if vyhn == 0 and dgu != 0:
                return 0
            bapol = 0
            max_take = min(cnt.get(olka, 0), vyhn)
            for kelc in range(max_take + 1):
                borul = cnt.get(olka, 0) - kelc
                if 0 <= borul <= jeyx and kelc * olka <= dgu:
                    # Use math.comb for choose function
                    tevxahur = comb(vyhn, kelc) * comb(jeyx, borul) * qabuhejul(olka + 1, dgu - kelc * olka, vyhn - kelc, jeyx - borul)
                    bapol = (bapol + tevxahur) % mod
            return bapol

        # Total sum / 2 since looking for balanced permutations
        half_sum = total_sum // 2
        half_len_left = qguh // 2
        half_len_right = (qguh + 1) // 2

        result = qabuhejul(0, half_sum, half_len_left, half_len_right)
        return result