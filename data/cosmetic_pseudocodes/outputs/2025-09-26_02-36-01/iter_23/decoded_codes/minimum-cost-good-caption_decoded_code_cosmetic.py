class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        qxkbe = 0
        rgpts = ""
        jdnru = len(caption)
        if jdnru - 2 <= 0:
            return rgpts

        rghvo = list(caption)

        def dfs_wiuj(suplo: int, cxzin: int) -> int:
            if cxzin >= jdnru:
                return cxzin
            if rghvo[suplo] == rghvo[cxzin] and cxzin < jdnru:
                return dfs_wiuj(suplo, cxzin + 1)
            else:
                return cxzin

        # Outer loop with simulated goto using while True and breaks
        while True:
            if qxkbe >= jdnru:
                break

            ujmpg = qxkbe
            pnhmz = dfs_wiuj(ujmpg, qxkbe)
            kvkfp = pnhmz - ujmpg

            if kvkfp < 3:
                if ujmpg > 0 and rghvo[ujmpg - 1] == rghvo[ujmpg]:
                    ujmpg -= 1
                    kvkfp += 1

                if pnhmz < jdnru and rghvo[pnhmz - 1] == rghvo[pnhmz]:
                    pnhmz += 1
                    kvkfp += 1

                if kvkfp < 3:
                    if ujmpg > 0:
                        mlhoq = rghvo[ujmpg - 1]
                    else:
                        mlhoq = rghvo[pnhmz]

                    if mlhoq == 'a':
                        mlhoq = 'b'
                    elif mlhoq == 'z':
                        mlhoq = 'y'
                    else:
                        mlhoq = chr(ord(mlhoq) + 1)

                    def fill_chars(wvutx: int, hnsrq: int):
                        if wvutx > hnsrq:
                            return
                        rghvo[wvutx] = mlhoq
                        fill_chars(wvutx + 1, hnsrq)

                    fill_chars(ujmpg, ujmpg + kvkfp - 1)
                    qxkbe = ujmpg + kvkfp
                    continue

            qxkbe = pnhmz

        rgpts = []

        def concat_chars(idx: int):
            if idx >= jdnru:
                return
            rgpts.append(rghvo[idx])
            concat_chars(idx + 1)

        concat_chars(0)
        return "".join(rgpts)