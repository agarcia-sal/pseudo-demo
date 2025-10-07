from typing import Collection, TypeVar, Union

T = TypeVar('T', bound=str)

def total_match(collection_alpha: Collection[T], collection_beta: Collection[T]) -> Union[Collection[T], Collection[T]]:
    length_sum_alpha: int = sum(len(element_char) for element_char in collection_alpha)
    length_sum_beta: int = sum(len(element_char) for element_char in collection_beta)
    return collection_alpha if length_sum_alpha <= length_sum_beta else collection_beta