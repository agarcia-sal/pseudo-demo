def main():
    # Read input from standard input
    inputString = input()

    # Normalize the path to eliminate redundant separators and up-level references
    normalizedPath = NormalizePath(inputString)

    # Remove leading slashes, ensuring only a single leading slash remains
    finalPath = RemoveLeadingSlashes(normalizedPath)

    # Output the final processed path
    print(finalPath)

def NormalizePath(path):
    # Use a method to convert backslashes to forward slashes
    # and remove unnecessary segments from the path
    path = path.replace('\\', '/')  # Convert backslashes to forward slashes
    pathSegments = path.split('/')
    
    normalizedSegments = []
    for segment in pathSegments:
        if segment == '' or segment == '.':
            continue  # Ignore empty segments and current directory symbols
        elif segment == '..':
            if normalizedSegments:
                normalizedSegments.pop()  # Remove the last segment for parent directory symbol
        else:
            normalizedSegments.append(segment)  # Add valid segments

    # Join segments and return the normalized path
    return '/' + '/'.join(normalizedSegments)

def RemoveLeadingSlashes(path):
    # If the path starts with one or more slashes, replace it with a single slash
    if path.startswith('/'):
        return '/' + path.lstrip('/')  # Keep one leading slash
    else:
        return path  # No leading slashes to remove

# Start the main function
main()
