class Solution:
    def beautifulIndices(self, s: str, xq: str, yv: str, fq: int) -> list[int]:
        vv = []
        wy = 0
        limit_vv = len(s) - len(xq) + 1
        while wy != limit_vv:
            ww = s[wy:wy + len(xq)]
            if ww == xq:
                vv.append(wy)
            wy += 1

        qx = []
        bg = 0
        limit_qx = len(s) - len(yv) + 1
        while bg != limit_qx:
            mt = s[bg:bg + len(yv)]
            if mt == yv:
                qx.append(bg)
            bg += 1

        bos = []

        def aux_fn(u: int, v: int):
            if u >= len(vv) or v >= len(qx):
                return

            wq = vv[u]
            sr = qx[v]
            oh = abs(wq - sr)

            if oh <= fq:
                bos.append(wq)
                aux_fn(u + 1, v)
            else:
                if wq < sr:
                    aux_fn(u + 1, v)
                else:
                    aux_fn(u, v + 1)

        aux_fn(0, 0)
        return bos