def main():
    # Step 1: Read two inputs
    string1 = input()  # First string input from user
    string2 = input()  # Second string input from user
    
    # Step 2: Remove spaces from both strings
    cleaned_string1 = string1.replace(" ", "")  # Remove spaces from string1
    cleaned_string2 = string2.replace(" ", "")  # Remove spaces from string2
    
    # Step 3: Initialize a list for character frequency differences
    frequency_differences = []
    
    # Step 4: Calculate frequency differences for each character
    for character_code in range(65, 123):  # ASCII codes from 'A' to 'z'
        count_in_string1 = cleaned_string1.count(chr(character_code))  # Count occurrences in cleaned_string1
        count_in_string2 = cleaned_string2.count(chr(character_code))  # Count occurrences in cleaned_string2
        difference = count_in_string1 - count_in_string2  # Calculate difference
        frequency_differences.append(difference)  # Add difference to the list
    
    # Step 5: Check if all differences are non-negative
    negative_counts = []  # List to track any negative differences
    
    for difference in frequency_differences:
        if difference < 0:  # If a difference is negative
            negative_counts.append(difference)  # Add to negative counts
    
    # Step 6: Determine if the modification is possible
    if len(negative_counts) == 0:  # No negative counts
        print("YES")  # The strings can be made equal
    else:
        print("NO")  # The strings cannot be made equal

# Call the main function to execute the program
main()
