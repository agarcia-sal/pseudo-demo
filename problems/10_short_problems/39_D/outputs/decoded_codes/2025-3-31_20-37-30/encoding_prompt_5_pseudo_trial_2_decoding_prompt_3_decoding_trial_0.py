def main():
    # Gather input from the user
    input1 = input()
    input2 = input()
    
    # Split the input strings into lists of numbers
    first_list = input1.split()
    second_list = input2.split()
    
    # Initialize a variable to count differences
    difference_count = 0

    # Loop through each index of the lists (assuming both lists have exactly 3 elements)
    for index in range(3):
        # Convert the current elements of both lists to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values at this index are different
        if first_value != second_value:
            # Increment the difference count
            difference_count += 1

    # After comparing all positions, decide on the output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is run as the main program
if __name__ == "__main__":
    main()


  1 2 3
  1 2 4
  

  YES
  

  3 2 1
  1 2 3
  

  NO
  