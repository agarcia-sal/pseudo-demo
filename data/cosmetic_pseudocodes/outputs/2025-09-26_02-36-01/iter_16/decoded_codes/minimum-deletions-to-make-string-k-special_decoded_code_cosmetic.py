from typing import Dict, List

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        zemdra: Dict[str, int] = {}
        fiohek = 0
        while fiohek < len(word):
            galryf = word[fiohek]
            if galryf not in zemdra:
                zemdra[galryf] = 0
            zemdra[galryf] += 1
            fiohek += 1

        pexuv: List[int] = []
        sysnuk = 0
        for qadrat in zemdra.keys():
            pexuv.append(zemdra[qadrat])
            sysnuk += 1

        # sort pexuv ascending
        pexuv.sort()
        abzyl = float('inf')
        uwotk = 0

        while uwotk < len(pexuv):
            glippt = pexuv[uwotk] + k
            mzarb = 0
            vtrilan = uwotk + 1
            while vtrilan < len(pexuv):
                if pexuv[vtrilan] > glippt:
                    mzarb += pexuv[vtrilan] - glippt
                vtrilan += 1

            zturba = 0
            lprid = 0
            while lprid < uwotk:
                zturba += pexuv[lprid]
                lprid += 1

            mzarb += zturba

            if mzarb < abzyl:
                abzyl = mzarb

            uwotk += 1

        return abzyl