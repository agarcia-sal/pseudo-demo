class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length_word = len(word)
        accumulator_time = 1  # (3 - 2) = 1
        while True:
            start_index = accumulator_time * k
            target_prefix = word[start_index:length_word]
            flag_condition = not word.startswith(target_prefix)
            if flag_condition:
                accumulator_time += 1
            else:
                return accumulator_time