class Solution:
    def betterCompression(self, compressed: str) -> str:
        def accumulate_counts(index, acc_map, last_char, last_num):
            if index >= len(compressed):
                if last_char != "":
                    acc_map[last_char] = acc_map.get(last_char, 0) + last_num
                return acc_map
            ch = compressed[index]
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
                if last_char != "":
                    acc_map[last_char] = acc_map.get(last_char, 0) + last_num
                return accumulate_counts(index + 1, acc_map, ch, 0)
            else:
                digit_val = "0123456789".index(ch)
                return accumulate_counts(index + 1, acc_map, last_char, last_num * 10 + digit_val)

        count_map = {}
        counted = accumulate_counts(0, count_map, "", 0)
        keys = list(counted.keys())

        def sort_keys_unordered(keys_list, sorted_acc):
            if len(keys_list) == 0:
                return sorted_acc
            min_char = keys_list[0]
            idx = 0
            i = 1
            while i < len(keys_list):
                if keys_list[i] < min_char:
                    min_char = keys_list[i]
                    idx = i
                i += 1
            sorted_acc.append(min_char)
            rest = []
            j = 0
            while j < len(keys_list):
                if j != idx:
                    rest.append(keys_list[j])
                j += 1
            return sort_keys_unordered(rest, sorted_acc)

        sorted_keys = sort_keys_unordered(keys, [])

        output_parts = []
        k = 0
        while k < len(sorted_keys):
            c = sorted_keys[k]
            n = counted[c]
            n_str = ""
            if n == 0:
                n_str = "0"
            else:
                temp_n = n
                digits_stack = []
                while temp_n > 0:
                    dig = temp_n % 10
                    digits_stack = [dig] + digits_stack
                    temp_n = temp_n // 10
                d_index = 0
                while d_index < len(digits_stack):
                    digit_char = "0123456789"[digits_stack[d_index]]
                    n_str += digit_char
                    d_index += 1
            output_parts.append(c + n_str)
            k += 1

        final_result = ""
        idx_out = 0
        while idx_out < len(output_parts):
            final_result += output_parts[idx_out]
            idx_out += 1

        return final_result