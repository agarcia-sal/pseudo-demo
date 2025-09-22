# Function to check character frequency differences between two strings
def check_character_frequencies():
    # Step 1: Get user input
    print("Enter the first string:")
    string1 = input()
    
    print("Enter the second string:")
    string2 = input()

    # Step 2: Clean the input strings by removing spaces
    clean_string1 = string1.replace(" ", "")
    clean_string2 = string2.replace(" ", "")

    # Step 3: Initialize a dictionary to hold frequency differences
    frequency_differences = {chr(i): 0 for i in range(ord('A'), ord('z') + 1)}

    # Step 4: Calculate the frequency of each character
    for character in frequency_differences.keys():
        count_in_string1 = clean_string1.count(character)
        count_in_string2 = clean_string2.count(character)
        frequency_differences[character] = count_in_string1 - count_in_string2

    # Step 5: Check if all frequency differences are non-negative
    negative_frequency_count = sum(1 for difference in frequency_differences.values() if difference < 0)

    # Step 6: Output the result based on frequency check
    if negative_frequency_count == 0:
        print("YES")
    else:
        print("NO")

# To execute the function
check_character_frequencies()
