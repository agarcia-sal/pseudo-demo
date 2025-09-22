def main():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of strings
    first_tokens = first_line.split()
    second_tokens = second_line.split()
    
    # Initialize a variable to count differences
    difference_count = 0 
    
    # Iterate over the first three elements of the token lists
    for index in range(3):
        # Convert string tokens to integers
        first_value = int(first_tokens[index])
        second_value = int(second_tokens[index])
        
        # Check for differences between the two values
        if first_value != second_value:
            difference_count += 1 
            
    # Assess the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    main()
