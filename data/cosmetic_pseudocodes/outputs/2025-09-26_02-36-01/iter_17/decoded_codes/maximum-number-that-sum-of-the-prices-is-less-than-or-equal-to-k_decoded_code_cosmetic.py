class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            blk_len = 1 << pos  # 2^pos
            full_blk = n // blk_len
            acc = (full_blk // 2) * blk_len
            if full_blk % 2 == 1:
                acc += (n % blk_len) + 1
            return acc

        def accumulated_price(n: int) -> int:
            sm = 0
            idx = 1
            while True:
                bit_pos = idx * x - 1
                cond_chk = 1 << bit_pos
                if cond_chk > n:
                    break
                sm += count_set_bits(n, bit_pos)
                idx += 1
            return sm

        lower_bound = 1
        upper_bound = 1 << 60  # 2^60
        while lower_bound <= upper_bound:
            middle = (lower_bound + upper_bound) // 2
            cur_price = accumulated_price(middle)
            if cur_price <= k:
                lower_bound = middle + 1
            else:
                upper_bound = middle - 1
        return upper_bound