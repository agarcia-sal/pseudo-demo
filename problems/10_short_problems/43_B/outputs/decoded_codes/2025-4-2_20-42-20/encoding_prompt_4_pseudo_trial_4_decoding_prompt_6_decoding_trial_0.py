# Function to check character frequency difference between two input strings
def check_character_frequency_difference():
    # Step 2: Initialize two empty lists for the strings
    string_one = []
    string_two = []

    # Step 3: Get user inputs and clean the strings
    for i in range(2):
        input_string = input()  # Step 3a: Read the input string
        cleaned_string = input_string.replace(" ", "")  # Step 3b: Remove all spaces
        if i == 0:
            string_one.append(cleaned_string)  # Step 3c: Store in string_one
        else:
            string_two.append(cleaned_string)  # Step 3c: Store in string_two
            
    # Extracting the cleaned strings for frequency calculation
    string_one = string_one[0]  # Getting the actual string from list
    string_two = string_two[0]  # Getting the actual string from list

    # Step 4: Initialize a frequency difference list
    freqs = []

    # Step 5: Calculate frequency difference for each character from 'A' to 'z'
    for char in range(ord('A'), ord('z') + 1):
        char_frequency_one = string_one.count(chr(char))  # Count in first string
        char_frequency_two = string_two.count(chr(char))  # Count in second string
        frequency_difference = char_frequency_one - char_frequency_two  # Step 5a
        freqs.append(frequency_difference)  # Step 5b: Store the difference in freqs
    
    # Step 6: Check for negative values in the freqs list
    if all(value >= 0 for value in freqs):  # If all values are non-negative
        print("YES")  # Step 6a: Output "YES"
    else:
        print("NO")  # Step 7a: Output "NO"

# Call the function to execute the character frequency check
check_character_frequency_difference()
