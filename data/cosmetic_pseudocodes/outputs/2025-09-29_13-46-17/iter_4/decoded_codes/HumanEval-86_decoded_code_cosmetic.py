from typing import List

def anti_shuffle(input_string: str) -> str:
    def accumulateSortedWords(idx: int, word_array: List[str], collected: List[str]) -> List[str]:
        if idx < len(word_array):
            current_word = word_array[idx]
            sorted_chars = sorted(current_word)
            recomposed_word = ''.join(sorted_chars)
            return accumulateSortedWords(idx + 1, word_array, collected + [recomposed_word])
        else:
            return collected

    wordsArr = input_string.split(" ")
    sortedWordsArr = accumulateSortedWords(0, wordsArr, [])
    outputStr = " ".join(sortedWordsArr)
    return outputStr