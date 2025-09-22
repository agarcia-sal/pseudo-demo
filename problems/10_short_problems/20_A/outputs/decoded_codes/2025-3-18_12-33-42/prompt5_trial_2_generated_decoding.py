def normalize_path():
    # Read the file path input from the user
    file_path = input()

    # Trim whitespace from the edges of the input string
    trimmed_path = file_path.strip()

    # Normalize the path
    normalized_path = []
    segments = trimmed_path.split('/')

    for segment in segments:
        if segment == '' or segment == '.':
            continue  # Skip empty segments and current directory indicators
        elif segment == '..':
            if normalized_path:
                normalized_path.pop()  # Remove the last valid segment for parent directory
        else:
            normalized_path.append(segment)  # Add valid segments

    # Join the normalized segments with a single slash
    final_path = '/' + '/'.join(normalized_path)

    # Output the final normalized path
    print(final_path)

# Example test cases ( Uncomment to test)
# Input: "///a/b//c/../d"
# Output: "/a/b/d"
# Input: "a/b/c/."
# Output: "/a/b/c"
# Input: "///"
# Output: "/"
# Input: "/../"
# Output: "/"
