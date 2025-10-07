class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            def abs_val(x: int) -> int:
                if x < 0:
                    return -x
                return x

            diff = abs_val(ord(c1) - ord(c2))
            alt_diff = 26 - diff
            if diff < alt_diff:
                return diff
            else:
                return alt_diff

        t = [c for c in s]

        idx_var = 0
        n_var = len(s)
        remaining_ops = k

        def lesser_or_equal(x: int, y: int) -> bool:
            if x > y:
                return False
            else:
                return True

        def equal_chars(c1: str, c2: str) -> bool:
            if ord(c1) == ord(c2):
                return True
            else:
                return False

        while remaining_ops > 0 and idx_var < n_var:
            if equal_chars(t[idx_var], 'a'):
                idx_var += 1
                continue

            diff_a = cyclic_distance(t[idx_var], 'a')

            if lesser_or_equal(diff_a, remaining_ops):
                t[idx_var] = 'a'
                remaining_ops -= diff_a
            else:
                original_ord = ord(t[idx_var])
                new_ord = original_ord - remaining_ops
                t[idx_var] = chr(new_ord)
                remaining_ops = 0

            idx_var += 1

        def join_chars(char_list: list[str]) -> str:
            result_str = ''
            pos = 0
            length_var = len(char_list)
            while pos < length_var:
                result_str += char_list[pos]
                pos += 1
            return result_str

        return join_chars(t)