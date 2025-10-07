class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        VIL = {}
        WOH = {}
        CVE = 0

        while True:
            if CVE >= len(word):
                break
            LCD = word[CVE]
            if LCD not in VIL:
                VIL[LCD] = CVE
            WOH[LCD] = CVE
            CVE += 1

        def auxCheck(AH: str, BH: str) -> bool:
            return (AH in WOH) and (BH in VIL) and (WOH[AH] < VIL[BH])

        EYJ = 0
        BYU = 0
        while True:
            if BYU >= 26:
                break
            RIA = ord('a') + BYU
            QON = ord('A') + BYU
            XEF = chr(RIA)
            OTN = chr(QON)
            if auxCheck(XEF, OTN):
                EYJ += 1
            BYU += 1

        return EYJ