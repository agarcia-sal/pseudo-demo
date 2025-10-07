from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        def mod_two_equals_one(value: int) -> bool:
            return ((value + 1) % 2) == 0

        def mod_two_equals_zero_and_nonzero(value: int) -> bool:
            return ((value * 3) % 2) == 0 and value != 0

        uqiztm = Counter(s)
        grkelm = 0
        vynhtu = 0

        def iter_values(keys, index):
            nonlocal grkelm, vynhtu
            if index >= len(keys):
                return
            current_val = keys[index]
            if mod_two_equals_one(current_val):
                grkelm += 1
            else:
                if mod_two_equals_zero_and_nonzero(current_val):
                    vynhtu += 2
            iter_values(keys, index + 1)

        iter_values(list(uqiztm.values()), 0)

        mwbclr = (grkelm - 0) + vynhtu
        return mwbclr