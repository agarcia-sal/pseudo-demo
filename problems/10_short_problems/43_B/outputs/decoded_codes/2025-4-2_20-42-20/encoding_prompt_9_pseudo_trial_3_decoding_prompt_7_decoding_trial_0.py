# Function to check if two strings are anagrams
def are_anagrams():
    # Step 1: Get User Input
    first_string = input()  # Prompt the user for the first string
    second_string = input()  # Prompt the user for the second string

    # Step 2: Remove Spaces
    string1 = first_string.replace(" ", "")  # Remove spaces from the first string
    string2 = second_string.replace(" ", "")  # Remove spaces from the second string

    # Step 3: Count Character Frequencies
    frequency_difference = []  # Initialize an empty list for frequency differences

    # Iterate through ASCII range for uppercase ('A') to lowercase ('z')
    for char in range(ord('A'), ord('z') + 1):  # Loop from ASCII 'A' to 'z'
        count_in_first = string1.count(chr(char))  # Count occurrences in the first string
        count_in_second = string2.count(chr(char))  # Count occurrences in the second string
        diff = count_in_first - count_in_second  # Calculate frequency difference
        frequency_difference.append(diff)  # Append the difference to the list

    # Step 4: Check Frequency Differences
    negative_count = sum(1 for diff in frequency_difference if diff < 0)  # Count negatives

    # Step 5: Generate Output
    if negative_count == 0:  # If there are no negative differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Otherwise, output "NO"

# Call the function
are_anagrams()
