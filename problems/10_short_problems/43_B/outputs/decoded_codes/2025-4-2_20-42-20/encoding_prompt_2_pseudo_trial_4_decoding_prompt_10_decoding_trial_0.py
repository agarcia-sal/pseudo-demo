def main():
    # Step 1: Receive Input and Clean Strings
    string1 = input().replace(" ", "")
    string2 = input().replace(" ", "")
    
    # Step 2: Initialize Frequency List
    frequencyDifferences = []

    # Step 3: Calculate Frequency Differences
    for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
        char = chr(ascii_value)  # Convert ASCII value to character
        count_in_string1 = string1.count(char)
        count_in_string2 = string2.count(char)
        
        # Calculate the difference and store it
        frequencyDifferences.append(count_in_string1 - count_in_string2)

    # Step 4: Check for Negative Differences
    negative_differences = [diff for diff in frequencyDifferences if diff < 0]
    
    # Output result based on the presence of negative differences
    if not negative_differences:
        print("YES")
    else:
        print("NO")

# Start the program
if __name__ == "__main__":
    main()
