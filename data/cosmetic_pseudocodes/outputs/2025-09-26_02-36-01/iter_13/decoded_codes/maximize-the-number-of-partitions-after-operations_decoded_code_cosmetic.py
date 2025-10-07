class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            alpha_base = ord('a')
            size_variable = 0
            distinct_set = {}
            count = 0

            def loop_chars(index: int):
                nonlocal size_variable, distinct_set, count
                if index == len(s):
                    return
                if size_variable < k:
                    if s[index] not in distinct_set:
                        distinct_set[s[index]] = True
                        size_variable += 1
                else:
                    if s[index] in distinct_set:
                        loop_chars(index + 1)
                        return
                    else:
                        count += 1
                        distinct_set.clear()
                        distinct_set[s[index]] = True
                        size_variable = 1
                loop_chars(index + 1)

            loop_chars(0)
            if size_variable > 0:
                count += 1
            return count

        result = max_partitions(s, k)
        pos = 0
        while pos < len(s):
            letter_code = ord('a')
            while True:
                if letter_code > ord('z'):
                    break
                candidate_char = chr(letter_code)
                if candidate_char == s[pos]:
                    letter_code += 1
                    continue

                prefix_str = []
                def build_prefix(idx: int):
                    if idx >= pos:
                        return
                    prefix_str.append(s[idx])
                    build_prefix(idx + 1)
                build_prefix(0)

                suffix_str = []
                def build_suffix(idx: int):
                    if idx >= len(s):
                        return
                    suffix_str.append(s[idx])
                    build_suffix(idx + 1)
                build_suffix(pos + 1)

                new_string = ''.join(prefix_str) + candidate_char + ''.join(suffix_str)
                comp = max_partitions(new_string, k)
                if comp > result:
                    result = comp
                letter_code += 1
            pos += 1
        return result