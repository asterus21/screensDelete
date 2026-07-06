"""
The repository contains a script to start another script to delete obsolete screenshots.
These screenshots are not used anymor in the PolyAnalyst User's Manual.
"""

import csv
import os
import subprocess
import sys


def start_script(input_path: str, output_path: str) -> None:
    """Starts the script to create two files with missed and unused screenshots."""
    subprocess.run(
        f"unused-images.exe --help-path {input_path} --output-path {output_path}",
        shell=True,
        check=False
    )


def read_file(file: str) -> list:
    """Opens the file and makes a Python list."""
    with open(file, "r", newline="", encoding="UTF-8") as f:
        data_list = list(csv.reader(f))
    return data_list


def fetch_items(files: list, path: str) -> list:
    """Creates a valid path for the images."""
    x = [f"{path}" + "/images/" + sublist[0] for sublist in files]
    return x


def delete_files(l: list) -> None:
    """Deletes files by an accepted path."""
    for file in l:
        try:
            os.path.exists(file)
            os.remove(file)
            print(f"File {file} deleted successfully.")
        except:
            print(f"File {file} does not exist.")
            sys.exit(0)


def main() -> None:
    """Main function."""
    input_path  = input("Enter the input path (e.g. D:/gitbash/help): ").strip()
    output_path = input("Enter the output path (e.g. ./): ").strip()
    start_script(input_path, output_path)
    # uncomment to delete files automatically
    # delete_files(fetch_items(read_file("unused.csv"), input_path))


if __name__ == "__main__":
    main()
