def main():
    # Read two lines of input
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists
    first_triplet = first_input.split()
    second_triplet = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of both triplets
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_triplet[index])
        second_value = int(second_triplet[index])
        
        # Check if the values are different
        if first_value != second_value:
            difference_count += 1
    
    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
if __name__ == "__main__":
    main()


     1 2 3
     1 2 3
     

     1 2 3
     1 2 4
     

     1 2 3
     4 2 3
     

     1 2 3
     4 5 6
     

     a b c
     1 2 3
     