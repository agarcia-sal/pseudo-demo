def main():
    # Read input values
    first_string = input()
    second_string = input()
    
    # Split the input strings into lists
    first_list = first_string.split() 
    second_list = second_string.split()
    
    # Initialize a mismatch counter
    mismatch_count = 0 
    
    # Compare the first three elements of both lists
    for index in range(3):  # Loop through the first three indexes
        first_value = int(first_list[index])  # Convert the element to integer
        second_value = int(second_list[index])  # Convert the element to integer
        
        # If the values do not match, increment the mismatch counter
        if first_value != second_value:
            mismatch_count += 1  # Increment count if mismatch found
    
    # Check the number of mismatches and print the result
    if mismatch_count < 3:
        print("YES")  # Provide output "YES" if number of mismatches is less than 3
    else:
        print("NO")  # Provide output "NO" if number of mismatches is 3 or more


# Entry point of the program
if __name__ == "__main__":
    main()  # Call main function to execute the program
