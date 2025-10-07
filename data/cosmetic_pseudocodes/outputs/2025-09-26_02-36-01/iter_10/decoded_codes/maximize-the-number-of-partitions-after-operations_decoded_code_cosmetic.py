class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            tally = 0
            chars_seen = set()
            pos = 0
            while pos < len(s):
                current_char = s[pos]
                if len(chars_seen) < k:
                    chars_seen.add(current_char)
                elif current_char in chars_seen:
                    pass
                else:
                    tally += 1
                    chars_seen = {current_char}
                pos += 1
            if chars_seen:
                tally += 1
            return tally

        result = max_partitions(s, k)

        def iterate_i(idx: int, limit: int) -> None:
            if idx >= limit:
                return

            def scan_new_char(ch_code: int) -> None:
                if ch_code > 122:
                    return
                ch = chr(ch_code)
                if ch == s[idx]:
                    scan_new_char(ch_code + 1)
                    return
                prefix = s[:idx]
                suffix = s[idx + 1 :]
                altered_str = prefix + ch + suffix
                candidate = max_partitions(altered_str, k)
                nonlocal result
                if candidate > result:
                    result = candidate
                scan_new_char(ch_code + 1)

            scan_new_char(97)
            iterate_i(idx + 1, limit)

        iterate_i(0, len(s))
        return result