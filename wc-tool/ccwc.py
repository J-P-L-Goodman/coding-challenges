import argparse


def count_bytes_in_file(file_path):
    try:
        with open(file_path, "rb") as file:
            bytes_count = len(file.read())

    except FileNotFoundError:
        print(f"ccwc -c: {file_path}: No such file or directory")
        return

    print(f"Bytes count: {bytes_count}; File: {file_path}")


def count_lines_in_file(file_path):
    try:
        with open(file_path, "rb") as file:
            line_count = sum(1 for line in file)

    except FileNotFoundError:
        print(f"ccwc -c: {file_path}: No such file or directory")
        return

    print(f"Line count: {line_count}; File: {file_path}")


def count_words_in_file(file_path):
    try:
        with open(file_path, "rb") as file:
            text = file.read()
            words = text.split()
            word_count = len(words)

    except FileNotFoundError:
        print(f"ccwc -c: {file_path}: No such file or directory")
        return
    print(f"Word count: {word_count}; File: {file_path}")


def count_characters_in_file(file_path):
    try:
        with open(file_path, "rb") as file:
            text = file.read()
            characters = len(text.decode())
    except FileNotFoundError:
        print(f"ccwc -c: {file_path}: No such file or directory")
        return
    print(f"Character count: {characters}; File: {file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count the number of bytes in a file.")
    parser.add_argument(
        "-c", "--count", help="Count bytes", default=False, action="store_true"
    )
    parser.add_argument(
        "-l", "--lines", help="Count lines", default=False, action="store_true"
    )
    parser.add_argument(
        "-w", "--words", help="Count words", default=False, action="store_true"
    )
    parser.add_argument(
        "-m",
        "--characters",
        help="Count characters",
        default=False,
        action="store_true",
    )
    parser.add_argument("file", help="File to count bytes  in")

    args = parser.parse_args()

    if args.count:
        count_bytes_in_file(args.file)
    elif args.lines:
        count_lines_in_file(args.file)
    elif args.words:
        count_words_in_file(args.file)
    elif args.characters:
        count_characters_in_file(args.file)
    else:
        count_bytes_in_file(args.file)
        count_lines_in_file(args.file)
        count_words_in_file(args.file)
