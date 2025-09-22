def compare_character_frequencies():
    # Step 1: Input two strings, removing any spaces
    s1 = input().replace(" ", "")
    s2 = input().replace(" ", "")
    
    # Step 2: Initialize a list for character frequency differences
    frequency_diff = [0] * (123)  # ASCII range from 'A' to 'z' covers codes 65 to 122
    
    # Step 3: Calculate frequency differences
    for char_code in range(65, 123):  # From 'A' (65) to 'z' (122)
        count_s1 = s1.count(chr(char_code))
        count_s2 = s2.count(chr(char_code))
        
        # Calculate the difference and store it
        frequency_diff[char_code] = count_s1 - count_s2
    
    # Step 4: Check for negative differences
    negative_count = sum(1 for diff in frequency_diff if diff < 0)
    
    # Step 5: Output the result based on negative_count
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
compare_character_frequencies()
