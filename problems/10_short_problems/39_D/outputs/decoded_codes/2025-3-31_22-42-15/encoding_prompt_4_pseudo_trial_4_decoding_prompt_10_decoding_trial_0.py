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
    for index in range(3):
        # Convert the string values to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # If the values do not match, increment the mismatch counter
        if first_value != second_value:
            mismatch_count += 1
            
    # Check the number of mismatches and print the result
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
