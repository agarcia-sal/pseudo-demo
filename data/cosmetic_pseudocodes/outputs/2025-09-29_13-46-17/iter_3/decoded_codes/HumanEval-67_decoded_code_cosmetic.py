from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def accumulateDigits(words: List[str], idx: int, collected: List[int]) -> List[int]:
        if idx >= len(words):
            return collected

        currentWord = words[idx]

        if not currentWord.isdigit():
            return accumulateDigits(words, idx + 1, collected)

        updatedCollected = collected + [int(currentWord)]
        return accumulateDigits(words, idx + 1, updatedCollected)

    wordsList = string_description.split(" ")
    digitsCollected = accumulateDigits(wordsList, 0, [])
    sumOfDigits = sum(digitsCollected)
    remainingFruits = total_number_of_fruits - sumOfDigits
    return remainingFruits