def CompareCharacterFrequencies():
    # Prompt the user to input the first string and remove spaces
    first_string = input()
    cleaned_first = ''.join(first_string.split())
    
    # Prompt the user to input the second string and remove spaces
    second_string = input()
    cleaned_second = ''.join(second_string.split())
    
    # Initialize the frequency differences list to hold counts for characters 'A' through 'z'
    frequencyDifferences = []
    
    # Loop through ASCII values of characters from 'A' (65) to 'z' (122)
    for char_code in range(65, 123):  # 65 to 122 (inclusive)
        # Count occurrences of the current character in each cleaned string
        count_first = cleaned_first.count(chr(char_code))
        count_second = cleaned_second.count(chr(char_code))
        
        # Calculate the difference in counts
        frequencyDifferences.append(count_first - count_second)
    
    # Check if all frequency differences are non-negative
    all_non_negative = all(diff >= 0 for diff in frequencyDifferences)
    
    # Output the result based on the frequency differences
    if all_non_negative:
        print("YES")
    else:
        print("NO")

# Example for testing the function
if __name__ == "__main__":
    CompareCharacterFrequencies()
