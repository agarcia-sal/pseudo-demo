def check_letter_frequencies():
    # Read two input strings from the user
    string1 = input()
    string2 = input()
    
    # Remove spaces from both strings
    cleaned_string1 = string1.replace(" ", "")
    cleaned_string2 = string2.replace(" ", "")

    # Initialize a list to store the frequency difference
    frequency_differences = []

    # Iterate over ASCII values from 'A' (65) to 'z' (122)
    for x in range(ord('A'), ord('z') + 1):
        # Count the occurrences of the character represented by x in both strings
        count_in_string1 = cleaned_string1.count(chr(x))
        count_in_string2 = cleaned_string2.count(chr(x))
        
        # Calculate the difference in frequencies and store it in the list
        frequency_difference = count_in_string1 - count_in_string2
        frequency_differences.append(frequency_difference)

    # Check if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Function to call the main function
check_letter_frequencies()
