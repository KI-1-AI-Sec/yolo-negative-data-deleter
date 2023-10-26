# YOLO Negative Data Deleter

This is a simple Python script which deletes negative training data (i.e. training images without any object classes present) by finding all empty label files and deleting them and their associated image files

## Usage


```bash
negative-data-deleter.py yolo_data_directory
```

usage: negative-data-deleter.py [-h] directory

Remove empty YOLO txt format label files and their associated images.

positional arguments:
  directory   Directory containing 'images' and 'labels' folders.

options:
  -h, --help  show this help message and exit