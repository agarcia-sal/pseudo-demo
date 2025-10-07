from typing import List


def filter_by_prefix(collection_of_words: List[str], pattern: str) -> List[str]:
    result_collection: List[str] = []

    def loop_through_items(index: int) -> None:
        if index < len(collection_of_words):
            def process_word() -> None:
                if collection_of_words[index].startswith(pattern):
                    result_collection.append(collection_of_words[index])
                loop_through_items(index + 1)
            process_word()

    loop_through_items(0)
    return result_collection