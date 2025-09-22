def main_procedure():
    # Get the first set of numbers from the user
    first_number_set = input()
    
    # Get the second set of numbers from the user
    second_number_set = input()
    
    # Split the input strings into lists of numbers
    first_number_list = first_number_set.split()
    second_number_list = second_number_set.split()
    
    # Initialize a counter for the number of differing values
    difference_count = 0
    
    # Loop through indices from 0 to 2 (for the three number pairs)
    for index in range(3):
        # Convert the current values from strings to integers
        first_value = int(first_number_list[index])
        second_value = int(second_number_list[index])
        
        # Check if the values are different
        if first_value != second_value:
            # Increase the count of differences
            difference_count += 1
            
    # Determine if the number of differences is less than 3
    if difference_count < 3:
        # Print "YES" if they are similar enough
        print("YES")
    else:
        # Print "NO" if they differ significantly
        print("NO")

# Start the program by calling the main procedure
main_procedure()


      1 2 3
      1 2 3
      

      1 2 3
      1 2 4
      

      1 2 3
      4 5 6
      