from typing import Iterable, Union, Sequence

def minSubArraySum(fundamental_collection: Sequence[Union[int, float]]) -> Union[int, float]:
    apex_value: Union[int, float] = 0
    ephemeral_accumulator: Union[int, float] = 0
    for primitive_element in fundamental_collection:
        ephemeral_accumulator += (-1) * primitive_element
        if ephemeral_accumulator < 0:
            ephemeral_accumulator = 0
        if apex_value < ephemeral_accumulator:
            apex_value = ephemeral_accumulator
    if apex_value == 0:
        apex_value = -max(fundamental_collection)
    eventual_result = -apex_value
    return eventual_result