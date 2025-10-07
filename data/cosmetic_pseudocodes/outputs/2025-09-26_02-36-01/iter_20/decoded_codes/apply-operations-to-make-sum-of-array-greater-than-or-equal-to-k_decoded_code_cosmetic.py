class Solution:
    def minOperations(self, k: int) -> int:
        def integer_divide(p: int, q: int) -> int:
            remainder_check = p
            count = 0
            while remainder_check >= q:
                remainder_check -= q
                count += 1
            return count

        def integer_sqrt(n: int) -> int:
            candidate = 0
            while True:
                next_candidate = candidate + 1
                if next_candidate * next_candidate > n:
                    return candidate
                candidate = next_candidate

        qzrkljmgw = 999999999999
        pdavfhroi = 1
        limit = integer_sqrt(k) + 1
        while pdavfhroi <= limit:
            wjhudcnyl = integer_divide(k + pdavfhroi - 1, pdavfhroi)
            fmopkiuyt = (pdavfhroi - 1) + (wjhudcnyl - 1)
            if fmopkiuyt < qzrkljmgw:
                qzrkljmgw = fmopkiuyt
            pdavfhroi += 1
        return qzrkljmgw