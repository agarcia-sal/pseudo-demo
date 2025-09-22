def doMain():
    # Read two strings from user input
    first_input = input()
    second_input = input()
    
    # Split the strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize the count of differences to zero
    differences_count = 0
    
    # Iterate through indices 0 to 2
    for index in range(3):
        # Convert values at the current index to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values are different
        if first_value != second_value:
            # Increment the differences count
            differences_count += 1
            
    # Check the number of differences to determine output
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    doMain()
