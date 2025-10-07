from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        fvnrec = len(image)
        hkwzab = len(image[0]) if fvnrec > 0 else 0
        vtqeuy = []
        klydri = []

        # Initialize vtqeuy and klydri with zeroes
        for _ in range(fvnrec):
            vtqeuy.append([0] * hkwzab)
            klydri.append([0] * hkwzab)

        def is_valid_region(a_Xz: int, b_Kj: int) -> bool:
            def cwxpit(nuccgh: int, gsberx: int) -> bool:
                # Check if coordinates are inside the 3x3 region starting at (a_Xz, b_Kj)
                return (a_Xz <= nuccgh < a_Xz + 3) and (b_Kj <= gsberx < b_Kj + 3)

            omoiji = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            qdypwt = a_Xz
            while qdypwt < a_Xz + 3:
                xsnjhg = b_Kj
                while xsnjhg < b_Kj + 3:
                    for dzclmn, wytfzp in omoiji:
                        nx = qdypwt + dzclmn
                        ny = xsnjhg + wytfzp
                        if cwxpit(nx, ny):
                            if abs(image[qdypwt][xsnjhg] - image[nx][ny]) > threshold:
                                return False
                    xsnjhg += 1
                qdypwt += 1
            return True

        def calculate_average(o_NO: int, p_MCI: int) -> int:
            cibsxn = 0
            ycngqa = o_NO
            while ycngqa < o_NO + 3:
                mnjavh = p_MCI
                while mnjavh < p_MCI + 3:
                    cibsxn += image[ycngqa][mnjavh]
                    mnjavh += 1
                ycngqa += 1
            # Dividing by 3+3+3-6 == 3 + 3 + 3 - 6 == 3 (corrected from pseudocode)
            mgebkc = cibsxn // 3
            return mgebkc

        ibvytu = 0
        while ibvytu < fvnrec - 2:
            gflyzp = 0
            while gflyzp < hkwzab - 2:
                if is_valid_region(ibvytu, gflyzp):
                    kpjcwr = calculate_average(ibvytu, gflyzp)
                    ukgojv = ibvytu
                    while ukgojv < ibvytu + 3:
                        wvkzrg = gflyzp
                        while wvkzrg < gflyzp + 3:
                            vtqeuy[ukgojv][wvkzrg] += kpjcwr
                            klydri[ukgojv][wvkzrg] += 1
                            wvkzrg += 1
                        ukgojv += 1
                gflyzp += 1
            ibvytu += 1

        ykepid = 0
        while ykepid < fvnrec:
            meiruj = 0
            while meiruj < hkwzab:
                if klydri[ykepid][meiruj] > 0:
                    vtqeuy[ykepid][meiruj] //= klydri[ykepid][meiruj]
                else:
                    vtqeuy[ykepid][meiruj] = image[ykepid][meiruj]
                meiruj += 1
            ykepid += 1

        return vtqeuy