def do_main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of string elements
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert strings to integers for comparison
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the elements are different
        if first_value != second_value:
            difference_count += 1
            
    # Determine the output based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    do_main()


  1 2 3
  1 2 3
  

  1 2 3
  4 2 3
  

  1 2 3
  4 5 6
  