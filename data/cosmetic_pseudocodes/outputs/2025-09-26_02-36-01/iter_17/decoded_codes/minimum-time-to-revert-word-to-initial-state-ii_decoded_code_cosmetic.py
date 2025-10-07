class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        w_len = len(word)
        t_counter = 1

        while True:
            sub_pref = word[t_counter * k : w_len]
            does_start = False

            if word.startswith(sub_pref):
                does_start = True

            if does_start:
                return t_counter

            t_counter += 1