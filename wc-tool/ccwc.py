import argparse


def count_bytes_in_file(file_path):
    bytes_count = 0

    try:
        with open(file_path, "rb") as file:
            bytes_count = len(file.read())

    except FileNotFoundError:
        print(f"ccwc -c: {file_path}: No such file or directory")
        return

    print(f"Bytes count: {bytes_count}; File: {file_path}")


def count_lines_in_file(file_path):
    try:
        with open(file_path, "r") as file:
            line_count = sum(1 for line in file)

    except FileNotFoundError:
        print(f"ccwc -c: {file_path}: No such file or directory")
        return

    print(f"Line count: {line_count}; File: {file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count the number of bytes in a file.")
    parser.add_argument(
        "-c", "--count", help="Count bytes", default=False, action="store_true"
    )
    parser.add_argument(
        "-l", "--lines", help="Count lines", default=False, action="store_true"
    )
    parser.add_argument("file", help="File to count bytes  in")

    args = parser.parse_args()

    if args.count:
        byte_count = count_bytes_in_file(args.file)
    if args.lines:
        lines_count = count_lines_in_file(args.file)
