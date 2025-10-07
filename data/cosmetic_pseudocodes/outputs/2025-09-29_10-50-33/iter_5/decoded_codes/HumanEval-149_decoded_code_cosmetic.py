from typing import List

def sorted_list_sum(collection_of_texts: List[str]) -> List[str]:
    collection_of_texts.sort()  # ascending order by default
    filtered_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(collection_of_texts):
        current_text = collection_of_texts[index_counter]
        if len(current_text) % 2 != 1:  # length not odd (i.e., even)
            filtered_collection.append(current_text)
        index_counter += 1
    return sorted(filtered_collection, key=len)