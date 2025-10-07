from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        alpha_map = Counter(word2)
        beta_map = Counter()
        demanded = 0
        fixed = len(alpha_map)
        pstart = 0
        results = 0

        def increase_counter(mapping, key):
            mapping[key] += 1

        def decrease_counter(mapping, key):
            if key in mapping:
                mapping[key] -= 1
                if mapping[key] == 0:
                    del mapping[key]

        qpos = 0
        while True:
            if qpos >= len(word1):
                break

            letter = word1[qpos]
            increase_counter(beta_map, letter)

            if letter in alpha_map:
                if beta_map[letter] == alpha_map[letter]:
                    demanded += 1

            while demanded == fixed and (qpos + 1 - pstart) >= len(word2):
                results += len(word1) - qpos
                left_letter = word1[pstart]
                decrease_counter(beta_map, left_letter)

                if left_letter in alpha_map:
                    if beta_map.get(left_letter, 0) < alpha_map[left_letter]:
                        demanded -= 1
                pstart += 1

            qpos += 1

        return results