class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        P = 10**9 + 1

        M = []
        a = 0
        while a <= 25:
            row = []
            b = 0
            while b <= 25:
                row.append(0)
                b += 1
            M.append(row)
            a += 1

        x = 0
        while x <= 25:
            y = 0
            while y < nums[x]:
                z = x + y + 1
                w = z % 26
                M[x][w] += 1
                y += 1
            x += 1

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            R = []
            i1 = 0
            while i1 <= 25:
                rowR = []
                j1 = 0
                while j1 <= 25:
                    rowR.append(0)
                    j1 += 1
                R.append(rowR)
                i1 += 1

            p1 = 0
            while p1 <= 25:
                q1 = 0
                while q1 <= 25:
                    r1 = 0
                    total = 0
                    while r1 <= 25:
                        temp_val = (A[p1][r1] * B[r1][q1]) % P
                        total += temp_val
                        r1 += 1
                    R[p1][q1] = (R[p1][q1] + total) % P
                    q1 += 1
                p1 += 1

            return R

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            id = []
            i2 = 0
            while i2 <= 25:
                row_id = []
                j2 = 0
                while j2 <= 25:
                    if i2 == j2:
                        row_id.append(1)
                    else:
                        row_id.append(0)
                    j2 += 1
                id.append(row_id)
                i2 += 1

            base_matrix = matrix
            expo = power
            while expo > 0:
                if expo % 2 == 1:
                    id = matrix_multiply(id, base_matrix)
                base_matrix = matrix_multiply(base_matrix, base_matrix)
                expo //= 2

            return id

        FM = matrix_power(M, t)

        cArr = []
        idx_c = 0
        while idx_c <= 25:
            cArr.append(0)
            idx_c += 1

        pos_c = 0
        while pos_c < len(s):
            ch_index = ord(s[pos_c]) - ord('a')
            cArr[ch_index] += 1
            pos_c += 1

        fArr = []
        idx_f = 0
        while idx_f <= 25:
            fArr.append(0)
            idx_f += 1

        aa = 0
        while aa <= 25:
            bb = 0
            while bb <= 25:
                val_calc = (cArr[aa] * FM[aa][bb]) % P
                sum_val = fArr[bb] + val_calc
                fArr[bb] = sum_val % P
                bb += 1
            aa += 1

        res_sum = 0
        cc = 0
        while cc <= 25:
            tempR = res_sum + fArr[cc]
            res_sum = tempR % P
            cc += 1

        return res_sum