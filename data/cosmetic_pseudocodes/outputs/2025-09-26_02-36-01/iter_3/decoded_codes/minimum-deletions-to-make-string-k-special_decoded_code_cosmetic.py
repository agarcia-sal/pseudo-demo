class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        char_counts = {}
        i = 0
        while i < len(word):
            current_char = word[i]
            if current_char in char_counts:
                char_counts[current_char] += 1
            else:
                char_counts[current_char] = 1
            i += 1

        counts_list = []
        itr = iter(char_counts.values())
        while True:
            try:
                val = next(itr)
                counts_list.append(val)
            except StopIteration:
                break

        counts_list.sort()
        min_del = 10 ** 1000
        pos = 0
        length = len(counts_list)
        while pos < length:
            max_freq = counts_list[pos] + k
            total_del = 0
            idx = pos + 1
            while idx < length:
                freq_val = counts_list[idx]
                if freq_val > max_freq:
                    total_del += freq_val - max_freq
                idx += 1

            front_idx = 0
            while front_idx < pos:
                total_del += counts_list[front_idx]
                front_idx += 1

            if total_del < min_del:
                min_del = total_del
            pos += 1

        return min_del