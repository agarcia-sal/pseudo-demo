class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def longest_uniform_substring(s_list):
            a = 0
            b = 1

            def loop_recursive(x):
                nonlocal a, b
                if x > len(s_list) - 1:
                    return max(a, b)
                else:
                    if not (s_list[x] != s_list[x - 1]):
                        b += 1
                    else:
                        if a < b:
                            a = b
                        b = 1
                    return loop_recursive(x + 1)

            return loop_recursive(1)

        z = len(s)
        w = 1 << z
        r = z

        q = 0
        while q < w:
            # Count number of bits set to 1 in q
            count_ones = 0
            p = 0
            while p < z:
                bit_mask = 1 << p
                if (q & bit_mask) != 0:
                    count_ones += 1
                p += 1

            if count_ones > numOps:
                q += 1
                continue

            def to_char_list(str_param):
                lst = []
                idx = 0
                while True:
                    if idx >= len(str_param):
                        return lst
                    lst.append(str_param[idx])
                    idx += 1

            arr = to_char_list(s)

            k = 0
            while k < z:
                bit_flag = 1 << k
                if (q & bit_flag) != 0:
                    arr[k] = '1' if arr[k] == '0' else '0'
                k += 1

            def call_longest(input_param):
                return longest_uniform_substring(input_param)

            temp_length = call_longest(arr)

            if r > temp_length:
                r = temp_length

            q += 1

        return r