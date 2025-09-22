def compare_strings():
    # Step 1: Input two strings from the user
    string_one = input()
    string_two = input()
    
    # Step 2: Process the strings by filtering out spaces
    filtered_string_one = [char for char in string_one if char != ' ']
    filtered_string_two = [char for char in string_two if char != ' ']

    # Step 3: Count character frequencies
    frequency_difference = []
    
    for ascii_value in range(ord('A'), ord('z') + 1):
        character = chr(ascii_value)
        count_one = filtered_string_one.count(character)
        count_two = filtered_string_two.count(character)
        # Calculate the difference in counts and store it
        frequency_difference.append(count_one - count_two)
    
    # Step 4: Check frequency conditions
    negative_counts = [count for count in frequency_difference if count < 0]

    # Step 5: Output the result based on the presence of negative counts
    if not negative_counts:
        print("YES")
    else:
        print("NO")

# Call the function to execute
compare_strings()
