def check_character_frequencies():
    # Step 1: Receive Input
    first_string = input()
    second_string = input()
    
    # Step 2: Process Input to Remove Spaces
    processed_first_string = [char for char in first_string if char != ' ']
    processed_second_string = [char for char in second_string if char != ' ']
    
    # Step 3: Initialize Frequency Count
    frequency_differences = [0] * (ord('z') - ord('A') + 1)  # Array to hold counts for A-Z and a-z
    
    # Step 4: Calculate Frequency Differences
    for i in range(ord('A'), ord('z') + 1):
        char = chr(i)
        count_first = processed_first_string.count(char)
        count_second = processed_second_string.count(char)
        frequency_differences[i - ord('A')] = count_first - count_second
    
    # Step 5: Determine Result
    if all(count >= 0 for count in frequency_differences):
        print("YES")
    else:
        print("NO")

# You can call the function to test the inputs
check_character_frequencies()
