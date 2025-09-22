# Step 1: Input Reading
first_string = input()  # Read the first input string
second_string = input()  # Read the second input string

# Step 2: String Preprocessing
cleaned_first_string = first_string.replace(" ", "")  # Remove spaces from the first string
cleaned_second_string = second_string.replace(" ", "")  # Remove spaces from the second string

# Step 3: Frequency Calculation
character_frequencies = []  # Initialize an empty list to hold frequency differences

# Iterate through the range of characters from 'A' to 'z'
for char in range(ord('A'), ord('z') + 1):
    first_count = cleaned_first_string.count(chr(char))  # Count occurrences in first string
    second_count = cleaned_second_string.count(chr(char))  # Count occurrences in second string
    frequency_difference = first_count - second_count  # Calculate the difference
    character_frequencies.append(frequency_difference)  # Append difference to the list

# Step 4: Result Evaluation
negative_count = sum(1 for frequency in character_frequencies if frequency < 0)  # Count negative differences

# Output the result based on the evaluation
if negative_count == 0:
    print("YES")  # All frequencies are non-negative
else:
    print("NO")  # There are some negative frequencies
