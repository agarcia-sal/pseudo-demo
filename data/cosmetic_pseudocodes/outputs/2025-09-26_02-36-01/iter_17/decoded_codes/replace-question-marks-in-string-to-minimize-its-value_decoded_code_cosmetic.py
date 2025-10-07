from collections import Counter

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        q_indices = []
        counts_map = Counter(s)
        if '?' in counts_map:
            del counts_map['?']

        for idx_var, ch in enumerate(s):
            if ch == '?':
                q_indices.append(idx_var)

        def find_min_char():
            min_val = float('inf')
            min_c = None
            for ch_iter in map(chr, range(ord('a'), ord('z') + 1)):
                count = counts_map.get(ch_iter, 0)
                if count < min_val:
                    min_val = count
                    min_c = ch_iter
            return min_c

        subs_list = []
        idx_j = 0
        while idx_j < len(q_indices):
            candidate_char = find_min_char()
            subs_list.append(candidate_char)
            counts_map[candidate_char] = counts_map.get(candidate_char, 0) + 1
            idx_j += 1

        sorted_subs = []
        for ch in subs_list:
            insert_pos = 0
            while insert_pos < len(sorted_subs) and sorted_subs[insert_pos] <= ch:
                insert_pos += 1
            sorted_subs.insert(insert_pos, ch)

        mutable_chars = list(s)
        replace_idx = 0
        sub_idx = 0
        while replace_idx < len(q_indices) and sub_idx < len(sorted_subs):
            mutable_chars[q_indices[replace_idx]] = sorted_subs[sub_idx]
            replace_idx += 1
            sub_idx += 1

        return ''.join(mutable_chars)