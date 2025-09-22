def frequency_comparison():
    # Step 1: Collect two lines of input
    first_input = input()
    second_input = input()

    # Step 2: Create a list of characters from the first input excluding spaces
    filtered_first = filtered_list(first_input)

    # Step 3: Create a list of characters from the second input excluding spaces
    filtered_second = filtered_list(second_input)

    # Step 4: Initialize frequency list
    frequency_differences = []

    # Step 5: Calculate frequency differences for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        character = chr(character_code)
        difference = filtered_first.count(character) - filtered_second.count(character)
        frequency_differences.append(difference)

    # Step 6: Check if any frequency difference is negative
    if any(diff < 0 for diff in frequency_differences):
        print("NO")
    else:
        print("YES")


def filtered_list(string):
    # Return a list of characters in string excluding spaces
    return [char for char in string if char != ' ']


# Testing the function with no direct input calls.
# If you wish to test it, simply uncomment the line below:
# frequency_comparison()
