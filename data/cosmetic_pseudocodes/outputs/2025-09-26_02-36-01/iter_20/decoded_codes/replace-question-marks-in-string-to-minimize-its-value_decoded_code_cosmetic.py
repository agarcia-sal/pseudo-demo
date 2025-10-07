class Solution:
    def minimizeStringValue(self, s):
        def custom_count_elements(sequence):
            accumulator = {}
            idx = 0
            while idx < len(sequence):
                element = sequence[idx]
                if element in accumulator:
                    accumulator[element] += 1
                else:
                    accumulator[element] = 1
                idx += 1
            return accumulator

        a1b2c3 = custom_count_elements(s)

        if '?' in a1b2c3:
            del a1b2c3['?']

        x9y8z7 = []
        u5v4w3 = 0
        while u5v4w3 < len(s):
            elt = s[u5v4w3]
            if elt == '?':
                x9y8z7.append(u5v4w3)
            u5v4w3 += 1

        m2n1o0 = []

        def alphabet_generator():
            c = 97
            while c <= 122:
                yield chr(c)
                c += 1

        def get_count_or_zero(mapping, key):
            if key in mapping:
                return mapping[key]
            else:
                return 0

        def increment_mapping(mapping, key):
            current_val = get_count_or_zero(mapping, key)
            mapping[key] = current_val + 1

        for pos_var in x9y8z7:
            lowest_val = float('inf')
            selected_char = None

            gen_iter = alphabet_generator()
            continue_loop = True
            while continue_loop:
                try:
                    char_iter = next(gen_iter)
                except StopIteration:
                    continue_loop = False
                    continue
                char_count_val = get_count_or_zero(a1b2c3, char_iter)
                if char_count_val < lowest_val:
                    lowest_val = char_count_val
                    selected_char = char_iter

            m2n1o0.append(selected_char)
            increment_mapping(a1b2c3, selected_char)

        def insertion_sort(sequence):
            pos_a = 1
            while pos_a < len(sequence):
                key_val = sequence[pos_a]
                pos_b = pos_a - 1
                while pos_b >= 0 and sequence[pos_b] > key_val:
                    sequence[pos_b + 1] = sequence[pos_b]
                    pos_b -= 1
                sequence[pos_b + 1] = key_val
                pos_a += 1

        insertion_sort(m2n1o0)

        l1m0n9 = []
        idx_seq = 0
        while idx_seq < len(s):
            l1m0n9.append(s[idx_seq])
            idx_seq += 1

        idx_c = 0
        while idx_c < len(x9y8z7):
            pos_index = x9y8z7[idx_c]
            repl_char = m2n1o0[idx_c]
            l1m0n9[pos_index] = repl_char
            idx_c += 1

        def join_characters(char_list):
            res_str = ''
            i_join = 0
            while i_join < len(char_list):
                res_str += char_list[i_join]
                i_join += 1
            return res_str

        return join_characters(l1m0n9)