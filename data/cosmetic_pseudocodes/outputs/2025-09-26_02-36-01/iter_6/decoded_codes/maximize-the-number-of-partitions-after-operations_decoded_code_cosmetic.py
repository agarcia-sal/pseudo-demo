class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            partitions_count = 0
            unique_set = set()

            def process_chars(index: int) -> None:
                nonlocal partitions_count, unique_set
                if index >= len(s):
                    return
                current_chr = s[index]
                if len(unique_set) < k:
                    unique_set.add(current_chr)
                    process_chars(index + 1)
                    return
                else:
                    if current_chr in unique_set:
                        process_chars(index + 1)
                        return
                    partitions_count += 1
                    unique_set = {current_chr}
                    process_chars(index + 1)

            process_chars(0)
            if len(unique_set) != 0:
                partitions_count += 1
            return partitions_count

        base_max = max_partitions(s, k)

        def iterate_pos(pos: int) -> None:
            nonlocal base_max
            if pos >= len(s):
                return

            def iterate_char(ch_val: int) -> None:
                nonlocal base_max
                if ch_val > ord('z'):
                    return
                ch = chr(ch_val)
                if ch != s[pos]:
                    prefix_str = ""
                    suffix_str = ""
                    if pos > 0:
                        prefix_str = s[:pos]
                    if pos + 1 <= len(s):
                        suffix_str = s[pos + 1:]
                    candidate = prefix_str + ch + suffix_str
                    candidate_max = max_partitions(candidate, k)
                    if candidate_max > base_max:
                        base_max = candidate_max
                iterate_char(ch_val + 1)

            iterate_char(ord('a'))
            iterate_pos(pos + 1)

        iterate_pos(0)
        return base_max