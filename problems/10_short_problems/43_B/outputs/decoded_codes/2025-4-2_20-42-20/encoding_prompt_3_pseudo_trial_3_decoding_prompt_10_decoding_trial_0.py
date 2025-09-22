def get_filtered_string(input_string):
    """Removes spaces from the input string and returns a list of characters."""
    return [char for char in input_string if char != ' ']

def count_character_frequencies(filtered_string):
    """Counts the frequencies of characters in the filtered string."""
    frequency_count = {}
    for char in filtered_string:
        if char in frequency_count:
            frequency_count[char] += 1
        else:
            frequency_count[char] = 1
    return frequency_count

def main():
    # Step 1: Read input
    first_string = input()
    second_string = input()

    # Step 2: Remove spaces from both strings
    filtered_first_string = get_filtered_string(first_string)
    filtered_second_string = get_filtered_string(second_string)

    # Step 3: Count character frequency differences
    frequency_first = count_character_frequencies(filtered_first_string)
    frequency_second = count_character_frequencies(filtered_second_string)

    # Step 4: Check frequency differences
    has_negative_difference = False
    
    for char in range(ord('A'), ord('z') + 1):
        character = chr(char)
        count_in_first = frequency_first.get(character, 0)
        count_in_second = frequency_second.get(character, 0)
        
        difference = count_in_first - count_in_second
        
        if difference < 0:
            has_negative_difference = True
            break

    # Step 5: Output the result
    if not has_negative_difference:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
