class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            def abs_val(x: int) -> int:
                return x if x >= 0 else -x

            diff = abs_val(ord(c1) - ord(c2))
            complement = 26 - diff
            return diff if diff < complement else complement

        def join_chars(chars: list[str]) -> str:
            acc = ""
            idx = 0
            limit = len(chars)
            while True:
                if idx >= limit:
                    break
                acc += chars[idx]
                idx += 1
            return acc

        temp_list = []
        idx_iter = 0
        len_s = len(s)

        def fill_list(pos: int) -> None:
            if pos >= len_s:
                return
            temp_list.append(s[pos])
            fill_list(pos + 1)

        fill_list(0)

        p = 0
        while True:
            if not (k > 0 and p < len_s):
                break
            if temp_list[p] == 'a':
                p += 1
                continue

            delta = cyclic_distance(temp_list[p], 'a')
            if delta <= k:
                temp_list[p] = 'a'
                k -= delta
            else:
                def char_code(ch: str) -> int:
                    return ord(ch)

                def char_from_code(code: int) -> str:
                    return chr(code)

                new_code = char_code(temp_list[p]) - k
                temp_list[p] = char_from_code(new_code)
                k = 0

            p += 1

        return join_chars(temp_list)