class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            tally = 0
            char_pool = set()
            idx = 0
            while idx < len(s):
                current_char = s[idx]
                if len(char_pool) < k:
                    char_pool.add(current_char)
                else:
                    if current_char in char_pool:
                        idx += 1
                        continue
                    else:
                        tally += 1
                        char_pool = {current_char}
                idx += 1
            if len(char_pool) != 0:
                tally += 1
            return tally

        outcome = max_partitions(s, k)
        pos = 0
        while True:
            if pos >= len(s):
                break
            letter_var = 'a'
            while letter_var <= 'z':
                if letter_var == s[pos]:
                    letter_var = chr(ord(letter_var) + 1)
                    continue
                prefix_str = s[:pos]
                suffix_str = s[pos + 1:]
                candidate_string = prefix_str + letter_var + suffix_str
                trial = max_partitions(candidate_string, k)
                if trial > outcome:
                    outcome = trial
                letter_var = chr(ord(letter_var) + 1)
            pos += 1
        return outcome