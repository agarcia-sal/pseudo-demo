def doMain():
    # Initialize variables to hold input strings and results
    input_string_1 = input()  # First input string containing numbers
    input_string_2 = input()  # Second input string containing numbers
    differences_count = 0  # Counter for differences

    # Split input strings into lists of strings
    list_1 = input_string_1.split()  # Split by space
    list_2 = input_string_2.split()  # Split by space
    
    # Loop to compare corresponding elements in the two lists
    for index in range(3):  # Loop over first three elements
        # Convert string elements to integers
        number_from_list_1 = int(list_1[index])
        number_from_list_2 = int(list_2[index])
        
        # Compare the two integers
        if number_from_list_1 != number_from_list_2:
            differences_count += 1  # Increment the count if they are different

    # Output result based on the count of differences
    if differences_count < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Entry point for program execution
if __name__ == "__main__":
    doMain()
