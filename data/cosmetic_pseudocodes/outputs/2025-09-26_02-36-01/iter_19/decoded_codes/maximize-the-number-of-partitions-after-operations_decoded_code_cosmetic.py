class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            running_total = 0
            collected_symbols = set()
            index_1 = 0  # zero-based index in Python
            length = len(s)
            while index_1 < length:
                current_token = s[index_1]
                if len(collected_symbols) < k:
                    collected_symbols.add(current_token)
                else:
                    if current_token in collected_symbols:
                        index_1 += 1
                        continue
                    else:
                        running_total += 1
                        collected_symbols = {current_token}
                index_1 += 1
            if collected_symbols:
                running_total += 1
            return running_total

        max_result = max_partitions(s, k)
        length = len(s)
        position = 0

        while position < length:
            char_code = 97  # 'a'
            while char_code <= 122:  # 'z'
                substitution = chr(char_code)
                if substitution == s[position]:
                    char_code += 1
                    continue
                new_string = s[:position] + substitution + s[position + 1:]
                temp_max = max_partitions(new_string, k)
                if temp_max > max_result:
                    max_result = temp_max
                char_code += 1
            position += 1

        return max_result