def doMain():
    # Read input values
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of strings
    input_list1 = first_input.split()
    input_list2 = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare elements from both lists
    for i in range(3):
        value1 = int(input_list1[i])
        value2 = int(input_list2[i])
        
        # Count the differences between the two values
        if value1 != value2:
            difference_count += 1
            
    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this code is run as a script
if __name__ == "__main__":
    doMain()


  1 2 3
  1 2 4
  

  5 6 7
  5 8 9
  