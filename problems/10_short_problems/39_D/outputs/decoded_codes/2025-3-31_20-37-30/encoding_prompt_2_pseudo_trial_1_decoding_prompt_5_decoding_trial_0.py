def doMain():
    # Read two strings from user input
    first_input = input()
    second_input = input()
    
    # Split the inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    differences_count = 0
    
    # Loop through the indices 0 to 2
    for index in range(3):
        # Convert the values to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values are different
        if first_value != second_value:
            differences_count += 1
    
    # Output "YES" or "NO" based on the number of differences
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the function if the script is run directly
if __name__ == "__main__":
    doMain()
