def main():
    # Read two lines of input from the user
    first_input = input()
    second_input = input()
    
    # Split each input string into a list of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # If the values are different, increment the difference counter
        if first_value != second_value:
            difference_count += 1
    
    # Determine the final output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()


   1 2 3
   1 2 4
   

   5 6 7
   5 6 7
   

   8 9 10
   1 2 3
   