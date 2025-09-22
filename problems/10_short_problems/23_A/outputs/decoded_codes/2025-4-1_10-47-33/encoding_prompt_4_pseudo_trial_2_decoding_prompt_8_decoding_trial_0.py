def read_input_line():
    return input().strip()  # Read a line and remove the trailing newline

def substring_exists(line, start_position, length):
    substring = line[start_position:start_position + length]
    return line.find(substring, start_position + 1) != -1

input_line = read_input_line()
line_length = len(input_line)
longest_repeated_length = 0

for substring_length in range(line_length):
    for starting_position in range(line_length):
        if substring_exists(input_line, starting_position, substring_length):
            longest_repeated_length = substring_length
            break  # Exit the inner loop as we found a repeated substring
    else:
        continue
    break  # Exit the outer loop if a repeated substring was found

print(longest_repeated_length)
