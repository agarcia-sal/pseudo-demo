def main():
    # Read two lines of input representing two sets of three scores
    first_input = input()
    second_input = input()

    # Split the inputs into separate elements (scores)
    first_scores = first_input.split()
    second_scores = second_input.split()

    # Initialize a counter for differing scores
    differing_score_count = 0 

    # Iterate through the three score pairs
    for index in range(3):  # Looping from 0 to 2
        # Convert the string scores to integers
        first_score = int(first_scores[index])
        second_score = int(second_scores[index])
        
        # Check if the scores differ
        if first_score != second_score:
            # Increment the count of differing scores
            differing_score_count += 1 
    
    # Determine if the number of differing scores is less than 3
    if differing_score_count < 3:
        print("YES")  # There are some matching scores
    else:
        print("NO")   # All scores differ

# Main execution starts here
main()
