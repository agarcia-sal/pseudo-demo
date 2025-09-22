def main():
    # Read two lines of input from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of strings
    first_tokens = first_input.split()
    second_tokens = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0 

    # Compare the corresponding elements of the two lists
    for index in range(3):
        # Convert the token to an integer
        first_value = int(first_tokens[index])
        second_value = int(second_tokens[index])
        
        # Check if the values are different
        if first_value != second_value:
            difference_count += 1 

    # Determine and print the result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()


  1 2 3
  1 2 4
  

  5 5 5
  5 5 5
  

  1 2 3
  4 5 6
  