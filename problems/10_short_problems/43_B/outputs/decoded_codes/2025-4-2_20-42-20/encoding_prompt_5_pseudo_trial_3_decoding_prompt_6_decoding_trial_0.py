# Function to compare character frequencies in two strings
def compare_character_frequencies():
    # Get the first string from the user and remove spaces
    first_string = input().replace(" ", "")
    # Get the second string from the user and remove spaces
    second_string = input().replace(" ", "")

    # Initialize a list to hold the frequency differences
    frequency_differences = []
    
    # Loop through ASCII values from 'A'(65) to 'z'(122)
    for char_code in range(65, 123):
        # Count occurrences of the character in both strings
        count_first = first_string.count(chr(char_code))
        count_second = second_string.count(chr(char_code))
        
        # Calculate the difference and store it
        frequency_differences.append(count_first - count_second)

    # Check if all differences are greater than or equal to zero
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")  # Frequencies match (first string has enough characters)
    else:
        print("NO")   # Frequencies do not match

# Call the function to execute
compare_character_frequencies()
