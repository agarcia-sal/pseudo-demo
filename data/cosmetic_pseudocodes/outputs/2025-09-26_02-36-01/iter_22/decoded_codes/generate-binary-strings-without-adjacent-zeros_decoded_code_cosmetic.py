from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        accepted = []

        def traverse(sequence: str):
            if len(sequence) == n:
                accepted.append(sequence)
                return

            lastItem = sequence[-1]

            if lastItem == "1":
                traverse(sequence + "0")
                traverse(sequence + "1")
            elif lastItem == "0":
                traverse(sequence + "1")

        traverse("0")
        traverse("1")

        return accepted