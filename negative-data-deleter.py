#!/usr/bin/env python3

import os
import argparse

def is_file_empty(file_path):
    with open(file_path, 'r') as file:
        # Check if content is just whitespace or empty
        return not file.read().strip()

def remove_empty_files(base_dir):
    # Directories for labels and images
    label_dir = os.path.join(base_dir, 'labels')
    image_dir = os.path.join(base_dir, 'images')

    # List of common extensions for images
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']

    # Loop through all txt files in the label directory
    for label_file in os.listdir(label_dir):
        label_path = os.path.join(label_dir, label_file)

        # Check if the file is "empty"
        if is_file_empty(label_path):
            # Remove the label file
            os.remove(label_path)
            print(f"Removed {label_path}")

            # Remove the corresponding image file
            base_name, _ = os.path.splitext(label_file)
            for ext in image_extensions:
                # Check both lowercase and uppercase extensions
                for possible_ext in [ext, ext.upper()]:
                    image_path = os.path.join(image_dir, base_name + possible_ext)
                    if os.path.exists(image_path):
                        os.remove(image_path)
                        print(f"Removed {image_path}")
                        break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove empty YOLO txt format label files and their associated images.")
    parser.add_argument("directory", help="Directory containing 'images' and 'labels' folders.")

    args = parser.parse_args()

    remove_empty_files(args.directory)
