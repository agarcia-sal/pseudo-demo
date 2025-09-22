def normalize_file_path():
    # Step 1: Receive Input
    filePath = input().strip()

    # Step 2: Normalize the File Path
    # Split the path into components, filter out any empty segments
    components = [segment for segment in filePath.split('/') if segment]

    # Join the components back together with a single '/'
    normalizedPath = '/'.join(components)

    # Step 3: Adjust the Path
    # Ensure the path starts with a single root slash
    finalPath = '/' + normalizedPath if normalizedPath else '/'

    # Step 4: Output the Result
    print(finalPath)

# Call the function to execute the normalization process
normalize_file_path()
