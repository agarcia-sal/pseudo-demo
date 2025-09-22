def main():
    # Read input values from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of components
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to count differences
    difference_count = 0
    
    # Compare corresponding elements of both lists
    for index in range(3):
        value_from_first_list = int(first_list[index])
        value_from_second_list = int(second_list[index])
        
        # Check for differences between the two values
        if value_from_first_list != value_from_second_list:
            difference_count += 1
    
    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")  # There are fewer than 3 differences
    else:
        print("NO")   # There are 3 or more differences

# Execute the main function when the script runs
if __name__ == "__main__":
    main()


  1 2 3
  1 2 3
  

  1 2 3
  4 2 3
  

  1 2 3
  4 5 6
  

  5 5 5
  1 1 1
  