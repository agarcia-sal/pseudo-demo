def doMain():
    # Collect input strings from the user
    first_input_string = input()
    second_input_string = input()
    
    # Split the input strings into lists
    first_input_list = first_input_string.split()
    second_input_list = second_input_string.split()
    
    # Initialize the count of differences
    difference_count = 0
    
    # Compare the first three elements of both lists
    for index in range(3):
        # Convert elements to integers
        first_value = int(first_input_list[index])
        second_value = int(second_input_list[index])
        
        # Check for differences
        if first_value != second_value:
            difference_count += 1
    
    # Evaluate the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Only execute doMain if the script is run directly
if __name__ == "__main__":
    doMain()
