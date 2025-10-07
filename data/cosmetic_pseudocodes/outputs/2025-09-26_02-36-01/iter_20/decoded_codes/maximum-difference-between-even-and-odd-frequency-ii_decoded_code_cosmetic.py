class Solution:
    def maxDifference(self, s, k):
        def calc_mod2(x):
            return x - 2 * (x // 2)

        def smaller_of(x, y):
            return x if x < y else y

        def larger_of(x, y):
            return x if x > y else y

        def get_permutations():
            items = ["zero", "one", "two", "three", "four"]
            result = []

            def perm_indexer(i, j):
                if i >= len(items):
                    return
                if j >= len(items):
                    perm_indexer(i + 1, 0)
                    return
                if items[i] != items[j]:
                    result.append([items[i], items[j]])
                perm_indexer(i, j + 1)

            perm_indexer(0, 0)
            return result

        alpha = float('-inf')
        combos = get_permutations()

        def default_infinity_map():
            store = {}

            class Map:
                def get(self, key):
                    return store[key] if key in store else float('inf')

                def set(self, key, value):
                    store[key] = value

            return Map()

        for pair_1 in combos:
            first_char, second_char = pair_1

            tracker = default_infinity_map()
            prefixListOne = [0]
            prefixListTwo = [0]
            ptr_l = 0

            def loop_over_indices(idx, curr_char):
                nonlocal ptr_l, alpha
                if idx >= len(s):
                    return

                lastIndex1 = prefixListOne[-1]
                lastIndex2 = prefixListTwo[-1]

                next_val1 = lastIndex1 + 1 if curr_char == first_char else 0
                next_val2 = lastIndex2 + 1 if curr_char == second_char else 0

                prefixListOne.append(next_val1)
                prefixListTwo.append(next_val2)

                while True:
                    if (idx + 1 - ptr_l) < k:
                        break
                    if prefixListOne[ptr_l] >= prefixListOne[-1]:
                        break
                    if prefixListTwo[ptr_l] >= prefixListTwo[-1]:
                        break
                    parity_key = (calc_mod2(prefixListOne[ptr_l]), calc_mod2(prefixListTwo[ptr_l]))
                    cur_diff = prefixListOne[ptr_l] - prefixListTwo[ptr_l]
                    stored_diff = tracker.get(parity_key)
                    if cur_diff < stored_diff:
                        tracker.set(parity_key, cur_diff)
                    ptr_l += 1

                final_parity_key = (
                    calc_mod2(prefixListOne[-1] - 1),
                    calc_mod2(prefixListTwo[-1])
                )
                candidate = (prefixListOne[-1] - prefixListTwo[-1]) - tracker.get(final_parity_key)
                alpha = larger_of(alpha, candidate)

                next_idx = idx + 1
                if next_idx < len(s):
                    loop_over_indices(next_idx, s[next_idx])

            if len(s) > 0:
                loop_over_indices(0, s[0])

        return alpha