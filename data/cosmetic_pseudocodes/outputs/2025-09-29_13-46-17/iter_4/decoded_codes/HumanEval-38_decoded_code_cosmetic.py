from typing import List


def encode_cyclic(input_string: str) -> str:
    def cycle_shift(chunk_list: List[str], current_index: int, collected: List[str]) -> List[str]:
        if current_index >= len(chunk_list):
            return collected
        current_chunk = chunk_list[current_index]
        if len(current_chunk) != 3:
            updated_collected = collected + [current_chunk]
        else:
            # rotate first character to the end
            rotated_chunk = current_chunk[1:3] + current_chunk[0]
            updated_collected = collected + [rotated_chunk]
        return cycle_shift(chunk_list, current_index + 1, updated_collected)

    def generate_chunks(source: str, position: int, result: List[str]) -> List[str]:
        if position >= len(source):
            return result
        end_pos = position + 3
        if end_pos > len(source):
            end_pos = len(source)
        extracted_chunk = source[position:end_pos]
        return generate_chunks(source, position + 3, result + [extracted_chunk])

    initial_chunks = generate_chunks(input_string, 0, [])
    transformed_chunks = cycle_shift(initial_chunks, 0, [])
    combined_string = "".join(transformed_chunks)
    return combined_string


def decode_cyclic(input_string: str) -> str:
    first_encode = encode_cyclic(input_string)
    return encode_cyclic(first_encode)