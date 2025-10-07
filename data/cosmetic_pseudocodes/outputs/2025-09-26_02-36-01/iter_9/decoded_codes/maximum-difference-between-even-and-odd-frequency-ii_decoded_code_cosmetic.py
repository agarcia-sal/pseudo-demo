class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def custom_defaultdict(default_val):
            store = {}

            def inner_get(key):
                if key not in store:
                    store[key] = default_val
                return store[key]

            def inner_set(key, val):
                store[key] = val

            return inner_get, inner_set

        def append_element(lst, val):
            new_lst = lst.copy()
            new_lst.append(val)
            return new_lst

        def remainder_mod_two(x):
            return x - ((x // 2) * 2)

        result = -9999999999999
        elements = ['z', 'e', 'n', 'o', 'r', 'u', 't', 'w', 'h', 'f']
        selected_chars = ['z', 'e', 'n', 'o', 'r']
        pairs = []

        def generate_pairs_with_diff_elements(chars):
            def helper(idx1, idx2, acc):
                if idx1 >= len(chars):
                    return acc
                if idx2 >= len(chars):
                    return helper(idx1 + 1, 0, acc)
                if chars[idx1] != chars[idx2]:
                    acc = acc + [(chars[idx1], chars[idx2])]
                return helper(idx1, idx2 + 1, acc)
            return helper(0, 0, [])

        pairs = generate_pairs_with_diff_elements(selected_chars)

        def enum_iter(iterable):
            result_list = []
            counter = 0

            def recurse_enum(idx_res):
                nonlocal counter, result_list
                if idx_res >= len(iterable):
                    return result_list
                pair_elem = (counter, iterable[idx_res])
                result_list = result_list + [pair_elem]
                counter += 1
                return recurse_enum(idx_res + 1)

            return recurse_enum(0)

        for tup in pairs:
            char_a, char_b = tup
            get_min, set_min = custom_defaultdict(999999999999)
            accPrefixA = [0]
            accPrefixB = [0]
            left_ptr = 0

            def process_inner(idx, tempAns):
                nonlocal accPrefixA, accPrefixB, left_ptr
                if idx >= len(s):
                    return tempAns
                curr_char = s[idx]
                lastA = accPrefixA[-1]
                lastB = accPrefixB[-1]
                if curr_char == char_a:
                    accPrefixA = append_element(accPrefixA, lastA + 1)
                else:
                    accPrefixA = append_element(accPrefixA, 0)
                if curr_char == char_b:
                    accPrefixB = append_element(accPrefixB, lastB + 1)
                else:
                    accPrefixB = append_element(accPrefixB, 0)

                def inner_while_loop(l_ref):
                    if (idx - l_ref + 1) < k:
                        return l_ref
                    if accPrefixA[l_ref] >= accPrefixA[-1]:
                        return l_ref
                    if accPrefixB[l_ref] >= accPrefixB[-1]:
                        return l_ref
                    key_tuple = (remainder_mod_two(accPrefixA[l_ref]), remainder_mod_two(accPrefixB[l_ref]))
                    curr_min = get_min(key_tuple)
                    if curr_min > accPrefixA[l_ref] - accPrefixB[l_ref]:
                        set_min(key_tuple, accPrefixA[l_ref] - accPrefixB[l_ref])
                    return inner_while_loop(l_ref + 1)

                left_ptr = inner_while_loop(left_ptr)
                p_key2 = (remainder_mod_two(accPrefixA[-1] - 1), remainder_mod_two(accPrefixB[-1]))
                val_diff = accPrefixA[-1] - accPrefixB[-1] - get_min(p_key2)
                if tempAns < val_diff:
                    tempAns = val_diff
                return process_inner(idx + 1, tempAns)

            result = process_inner(0, result)

        return result