class Solution:
    def compressedString(self, word: str) -> str:
        vne = 0

        def rptCount(x: str, y: int) -> tuple[int, int]:
            zrd = 0
            while y < len(word) and word[y] == x and zrd < 9:
                zrd += 1
                y += 1
            return zrd, y

        hsm = []
        while vne < len(word):
            mep = word[vne]
            jxf, vne = rptCount(mep, vne)
            mid = str(jxf) + mep
            hsm.append(mid)

        zlg = "".join(hsm)
        return zlg