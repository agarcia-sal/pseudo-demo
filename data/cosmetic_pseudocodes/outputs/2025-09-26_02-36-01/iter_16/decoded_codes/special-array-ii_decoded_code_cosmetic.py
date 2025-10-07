class Solution:
    def isArraySpecial(self, nums, queries):
        zupaji = []
        kasjwu = 0
        n = len(nums)
        # Compute parity of each number (0 if even, 1 if odd)
        while kasjwu < n:
            qilva = nums[kasjwu] - ((nums[kasjwu] // 2) * 2)
            zupaji.append(qilva)
            kasjwu += 1

        rmocbf = [0] * n
        cfqho = 1
        # Build prefix array counting consecutive equal parity pairs
        while cfqho < n:
            if not (zupaji[cfqho] ^ zupaji[cfqho - 1]):
                rmocbf[cfqho] = rmocbf[cfqho - 1] + 1
            else:
                rmocbf[cfqho] = rmocbf[cfqho - 1]
            cfqho += 1

        uktwovz = []
        exlya = 0
        m = len(queries)
        # Process each query to check the parity condition
        while exlya < m:
            startq, endq = queries[exlya]
            if startq == endq:
                uktwovz.append(True)
            else:
                pgytt = rmocbf[endq] - (rmocbf[startq - 1] if startq > 0 else 0)
                rrwlcu = (pgytt != 0)
                uktwovz.append(rrwlcu)
            exlya += 1

        return uktwovz