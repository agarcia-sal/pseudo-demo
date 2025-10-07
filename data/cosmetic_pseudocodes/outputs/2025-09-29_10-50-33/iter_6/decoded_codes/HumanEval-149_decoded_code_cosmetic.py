from typing import List


def sorted_list_sum(collection_of_texts: List[str]) -> List[str]:
    filtered_collection: List[str] = []

    def process_item(index: int) -> None:
        if index >= len(collection_of_texts):
            return
        if len(collection_of_texts[index]) % 2 == 0:
            filtered_collection.append(collection_of_texts[index])
        process_item(index + 1)

    collection_of_texts.sort()  # sort alphabetically ascending
    process_item(0)

    return sorted(filtered_collection, key=len)