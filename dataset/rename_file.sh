#!/bin/bash

# 이 파일은 한 폴더내에 이미지들의 이름이 순서대로 되어있지 않으면 쭉 이름이 이어지도록 해주는 파일이다.

# Directory where the files are located
directory="./fail"  # Replace with the path to your directory

# Change to the directory
cd "$directory" || exit

# List files starting with cor_ and ending with .jpg, sorted numerically
files=$(ls fail_*.jpg | sort -t_ -k2 -n)

# Initialize counter
counter=0

# Loop through each file and rename it sequentially
for file in $files; do
    # Generate new file name with zero-padded number
    new_name=$(printf "fail_%04d.jpg" "$counter")
    
    # Rename the file
    mv "$file" "$new_name"
    
    # Increment counter
    counter=$((counter + 1))
done

echo "Renaming complete!"
