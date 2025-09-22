# Function to check the frequency of characters in two strings
def compare_string_frequencies():
    # Step 1: Receive Input
    firstString = input()  # Read the first string from input
    secondString = input()  # Read the second string from input

    # Step 2: Process Input Strings
    # Remove spaces from the strings
    firstProcessed = firstString.replace(" ", "")
    secondProcessed = secondString.replace(" ", "")

    # Step 3: Initialize Frequency List
    # The frequency difference list holds the count differences for each character
    frequencyDifference = [0] * 256  # Initialize for ASCII range

    # Step 4: Calculate Character Frequencies
    for char in firstProcessed:
        frequencyDifference[ord(char)] += 1  # Increment count for first string

    for char in secondProcessed:
        frequencyDifference[ord(char)] -= 1  # Decrement count for second string

    # Step 5: Check Conditions
    negative_count = 0  # Count of negative differences

    for count in frequencyDifference:
        if count < 0:
            negative_count += 1  # Count how many characters are more in second string

    # Determine if firstProcessed meets or exceeds secondProcessed
    if negative_count == 0:
        print("YES")  # All characters in firstProcessed meet/exceed those in secondProcessed
    else:
        print("NO")  # Some characters in secondProcessed exceed those in firstProcessed

# Call the function to execute
compare_string_frequencies()
