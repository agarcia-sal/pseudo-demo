def main():
    # Read input values
    first_line = input()  # Input expected in a single line for the first list
    second_line = input()  # Input expected in a single line for the second list
    
    # Split input lines into lists of strings
    list1 = first_line.split()
    list2 = second_line.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        value_a = int(list1[index])  # Convert to integer
        value_b = int(list2[index])  # Convert to integer
        
        # Check if values are different
        if value_a != value_b:
            # Increment the difference counter
            difference_count += 1
            
    # Check the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    main()


  1 2 3
  1 2 4
  

  YES
  

  1 2 3
  4 5 6
  

  NO
  