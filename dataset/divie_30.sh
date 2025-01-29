#!/bin/bash

# Set the directory containing the .jpg files
directory="./fail"

# Change to the directory containing the .jpg files
cd "$directory" || exit

# List all .jpg files and sort them
files=($(ls fail_*.jpg 2>/dev/null | sort))

# Get the total number of files
total_files=${#files[@]}

# Initialize a counter for the folder number
folder_counter=1

# Loop through the files and move them into folders
for ((i=0; i<$total_files; i+=30)); do
    folder_name=$(printf "folder_%03d" "$folder_counter")
    
    # Create a folder for this batch of 30 files
    mkdir -p "$folder_name"
    
    # Move 30 files into the new folder
    for ((j=i; j<i+30 && j<$total_files; j++)); do
        mv "${files[$j]}" "$folder_name/"
    done
    
    # Increment the folder counter
    folder_counter=$((folder_counter + 1))
done

echo "Files have been divided into folders."
