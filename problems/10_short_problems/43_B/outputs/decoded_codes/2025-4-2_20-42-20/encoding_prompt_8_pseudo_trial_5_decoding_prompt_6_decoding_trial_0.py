# Function to check if the two strings can be made equal by removing spaces
def main():
    # Step 1: Read two inputs from the user
    string1 = input()
    string2 = input()
    
    # Step 2: Remove spaces from both strings
    cleaned_string1 = string1.replace(" ", "")
    cleaned_string2 = string2.replace(" ", "")
    
    # Step 3: Initialize a list for character frequency differences
    frequency_differences = []
    
    # Step 4: Calculate frequency differences for each character from A (65) to z (122)
    for character_code in range(65, 123):  # ASCII values from 'A' to 'z'
        count_in_string1 = cleaned_string1.count(chr(character_code))
        count_in_string2 = cleaned_string2.count(chr(character_code))
        
        # Calculate the difference and store it in the frequency differences list
        difference = count_in_string1 - count_in_string2
        frequency_differences.append(difference)
    
    # Step 5: Check if all differences are non-negative
    negative_counts = []
    
    for difference in frequency_differences:
        if difference < 0:
            negative_counts.append(difference)
    
    # Step 6: Determine if the modification is possible
    if len(negative_counts) == 0:
        print("YES")  # The strings can be made equal
    else:
        print("NO")   # The strings cannot be made equal

# Execute the main function
main()
