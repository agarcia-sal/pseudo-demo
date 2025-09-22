def main():
    # Read two lines of input from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop to compare the first three elements from both input lists
    for index in range(3):  # Loop through the first three indices
        # Convert the current elements to integers for comparison
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check if the values are different
        if first_value != second_value:
            # Increment the counter if they differ
            difference_count += 1
            
    # Check the total count of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
main()


  1 2 3
  1 2 4
  

  5 6 7
  8 9 7
  

  10 20 30
  10 20 30
  