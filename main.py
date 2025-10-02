import csv
import os
import subprocess


def start_script(input_path: str, output_path: str) -> None:

    """Starts the script to create two files with missed and unused screenshots."""

    subprocess.run(
        f"unused-images.exe --help-path {input_path} --output-path {output_path}",
        shell=True,
    )


def read_file(file: str) -> list:

    """Opens the file and makes a Python list."""

    with open(file, "r", newline="") as f:
        csv_reader = csv.reader(f)
        data_list = list(csv_reader)
    return data_list


def fetch_items(l: list, p: str) -> list:

    """Creates a valid path for the images."""

    x = [f"{p}" + "/images/" + sublist[0] for sublist in l]
    return x


def delete_files(l: list) -> None:

    """Deletes files by an accepted path."""

    for file in l:
        if os.path.exists(file):
            os.remove(file)
            print(f"File {file} deleted successfully.")
        else:
            print(f"File {file} does not exist.")


def main() -> None:

    """Main function."""

    input_path = input("Enter the input path (e.g. D:/gitbash/help): ").strip()
    output_path = input("Enter the output path (e.g. ./): ").strip()

    start_script(input_path, output_path)
    delete_files(fetch_items(read_file("unused.csv"), input_path))


if __name__ == "__main__":
    main()
