class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            visited_set = set()
            cnt_parts = 0

            def process_char(pos: int):
                nonlocal cnt_parts, visited_set
                if pos == len(s):
                    return
                if len(visited_set) < k:
                    visited_set.add(s[pos])
                    process_char(pos + 1)
                    return
                else:
                    if s[pos] in visited_set:
                        process_char(pos + 1)
                        return
                    else:
                        cnt_parts += 1
                        visited_set = {s[pos]}
                        process_char(pos + 1)
                        return

            process_char(0)

            if len(visited_set) > 0:
                cnt_parts += 1
            return cnt_parts

        best_count = max_partitions(s, k)

        def loop_i(i_cur: int):
            nonlocal best_count
            if i_cur > len(s) - 1:
                return

            def loop_c(c_ascii: int):
                nonlocal best_count
                if c_ascii > 122:
                    return
                current_letter = chr(c_ascii)
                if current_letter == s[i_cur]:
                    loop_c(c_ascii + 1)
                    return
                before_part = s[:i_cur] if i_cur > 0 else ""
                after_part = s[i_cur + 1 :] if i_cur < len(s) - 1 else ""
                candidate_string = before_part + current_letter + after_part
                candidate_count = max_partitions(candidate_string, k)
                if candidate_count > best_count:
                    best_count = candidate_count
                loop_c(c_ascii + 1)
                return

            loop_c(97)
            loop_i(i_cur + 1)
            return

        loop_i(0)

        return best_count