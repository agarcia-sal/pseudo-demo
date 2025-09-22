def doMain():
    # Step 2: Input collection
    first_input_string = input()
    second_input_string = input()
    
    # Step 3: String splitting
    first_input_list = first_input_string.split()
    second_input_list = second_input_string.split()
    
    # Step 4: Result initialization
    difference_count = 0
    
    # Step 5: Comparison loop
    for index in range(3):  # Only comparing the first three elements (indices 0, 1, 2)
        first_value = int(first_input_list[index])  # Convert first list's element to integer
        second_value = int(second_input_list[index])  # Convert second list's element to integer
        
        if first_value != second_value:  # Check for inequality
            difference_count += 1  # Increment count of differences

    # Step 6: Result evaluation
    if difference_count < 3:
        print("YES")  # Print message if fewer than 3 differences
    else:
        print("NO")  # Print message if 3 or more differences

# Step 7: Execution trigger
if __name__ == "__main__":
    doMain()  # Call the main function when the script is executed
