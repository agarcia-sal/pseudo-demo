class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def increment_map(mapp, key):
            mapp[key] = mapp.get(key, 0) + 1

        def decrement_map(mapp, key):
            mapp[key] = mapp.get(key, 0) - 1
            if mapp[key] <= 0:
                del mapp[key]

        def exists_ge_k(mapp, threshold):
            for val in mapp.values():
                if val >= threshold:
                    return True
            return False

        def recur(r_index, total_so_far, left_pos, freq_m):
            if r_index == len(s):
                return total_so_far

            increment_map(freq_m, s[r_index])

            while exists_ge_k(freq_m, k):
                decrement_map(freq_m, s[left_pos])
                left_pos += 1

            return recur(r_index + 1, total_so_far + left_pos, left_pos, freq_m)

        return recur(0, 0, 0, {})