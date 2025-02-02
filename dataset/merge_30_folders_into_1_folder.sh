#!/bin/bash

# 이 파일은 한 폴더내에 이미지를 30장씩 폴더들을 하나의 폴더로 묶어주는 파일이다.

# Set the target directory where all images will be moved
target_directory="./"

# Create the target directory if it doesn't exist
mkdir -p "$target_directory"

# Set the directory containing the folders with images
directory="./fail"

# Change to the directory containing the folders
cd "$directory" || exit

# Move all .jpg files from each folder into the target directory
for folder in */; do
    mv "$folder"*.jpg "$target_directory/"
    
    # Optionally, remove the now-empty folder
    rmdir "$folder"
done

echo "All images have been moved to $target_directory."
