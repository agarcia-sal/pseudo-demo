def compare_character_frequencies():
    # Read input strings from the user
    first_input_string = input()
    second_input_string = input()
    
    # Remove spaces from both input strings and create lists of characters
    first_string_characters = [char for char in first_input_string if char != ' ']
    second_string_characters = [char for char in second_input_string if char != ' ']
    
    # Initialize a list to hold frequency differences for each ASCII character
    frequency_differences = []

    # Loop through ASCII values for characters from 'A' to 'z'
    for x in range(ord('A'), ord('z') + 1):
        # Calculate the frequency of character and add to frequency_differences
        difference = first_string_characters.count(chr(x)) - second_string_characters.count(chr(x))
        frequency_differences.append(difference)

    # Check if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")


      a b c
      a b c
      

      a b c
      a b c d
      

      Hello World
      Hello
      