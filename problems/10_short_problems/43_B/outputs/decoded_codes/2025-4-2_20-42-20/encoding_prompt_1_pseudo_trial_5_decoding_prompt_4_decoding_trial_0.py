def main():
    # Step 1: Read Input
    string1 = input()
    string2 = input()
    
    # Step 2: Remove Spaces
    cleaned_string1 = [char for char in string1 if char != ' ']
    cleaned_string2 = [char for char in string2 if char != ' ']
    
    # Step 3: Initialize Frequency Difference List
    frequency_differences = []
    
    # Step 4: Calculate Frequency Differences
    for char_code in range(ord('A'), ord('z') + 1):
        char = chr(char_code)  # Convert ASCII code to character
        
        count1 = cleaned_string1.count(char)  # Count in cleaned_string1
        count2 = cleaned_string2.count(char)  # Count in cleaned_string2
        
        # Calculate the frequency difference and add to the list
        frequency_differences.append(count1 - count2)

    # Step 5: Check Frequency Differences
    negative_count = sum(1 for difference in frequency_differences if difference < 0)

    # Step 6: Output Result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# This will allow the function to run when executed
if __name__ == "__main__":
    main()
