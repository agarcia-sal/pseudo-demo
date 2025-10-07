from typing import List, Set


def select_words(text_p: str, count_m: int) -> List[str]:
    vowels_set: Set[str] = {"a", "e", "i", "o", "u"}
    output_collection: List[str] = []

    def analyze(idx: int) -> None:
        if idx >= len(text_p):
            return

        parts_list = text_p.split(" ")
        position = 0

        def iterate_words(pos: int) -> None:
            if pos >= len(parts_list):
                return

            item = parts_list[pos]
            cons_counter = 0
            char_index = 0

            while char_index < len(item):
                char_lower = item[char_index].lower()
                if char_lower not in vowels_set:
                    cons_counter += 1
                char_index += 1

            if cons_counter == count_m:
                output_collection.append(item)

            iterate_words(pos + 1)

        iterate_words(position)

    analyze(0)
    return output_collection