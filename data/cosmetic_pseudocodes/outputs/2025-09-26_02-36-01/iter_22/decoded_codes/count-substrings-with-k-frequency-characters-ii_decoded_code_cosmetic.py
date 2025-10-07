class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def adjustCount(mapping_ref: dict, key_val: str, delta_val: int) -> None:
            if key_val in mapping_ref:
                mapping_ref[key_val] += delta_val
            else:
                if delta_val > 0:
                    mapping_ref[key_val] = delta_val
            if key_val in mapping_ref and mapping_ref[key_val] == 0:
                del mapping_ref[key_val]

        accumulator = 0
        tracker = dict()
        front = 0
        back = 0

        while back < len(s):
            adjustCount(tracker, s[back], 1)

            while any(count >= k for count in tracker.values()):
                adjustCount(tracker, s[front], -1)
                front += 1

            accumulator += front
            back += 1

        return accumulator