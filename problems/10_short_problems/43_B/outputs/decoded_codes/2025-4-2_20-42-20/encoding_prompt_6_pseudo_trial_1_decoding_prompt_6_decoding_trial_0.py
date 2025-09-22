def check_character_distribution():
    # Step 1: Read two strings from user input and remove spaces
    first_string = input().replace(" ", "")
    second_string = input().replace(" ", "")

    # Step 2: Initialize an array to hold frequency differences
    # We will use a dictionary to handle character counts
    frequency_differences = {chr(i): 0 for i in range(65, 123)}  # ASCII values for 'A' to 'z'

    # Step 3: Calculate the frequency difference for each character
    for char in frequency_differences.keys():
        count_first = first_string.count(char)  # Count occurrences in first_string
        count_second = second_string.count(char)  # Count occurrences in second_string
        # Calculate the difference and store it
        frequency_differences[char] = count_first - count_second

    # Step 4: Check if any character has a negative frequency difference
    negative_difference_count = 0
    for difference in frequency_differences.values():
        if difference < 0:  # If any frequency difference is negative
            negative_difference_count += 1  # Increment the count of negative differences

    # Step 5: Determine if the character distributions are valid
    if negative_difference_count == 0:
        print("YES")  # first_string can cover second_string
    else:
        print("NO")   # first_string cannot cover second_string

# Example of running the function (you can replace this with actual testing)
check_character_distribution()
