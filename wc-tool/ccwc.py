import argparse
import sys


def count_bytes_in_text(text):
    bytes_count = len(text.encode())
    return bytes_count


def count_lines_in_text(text):
    line_count = text.count("\n") + 1
    return line_count


def count_words_in_text(text):
    words = text.split()
    word_count = len(words)
    return word_count


def count_characters_in_text(text):
    characters = len(text)
    return characters


def main():
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
    parser.add_argument("file", help="File to count in", nargs="?")

    args = parser.parse_args()

    if args.file is None:
        # No filename provided, read from standard input
        text = sys.stdin.read()
    else:
        with open(args.file, "rb") as file:
            text = file.read().decode("utf-8")

    if args.count:
        bytes_count = count_bytes_in_text(text)
        print(f"Bytes count: {bytes_count}; File: {args.file or 'Standard Input'}")

    if args.lines:
        line_count = count_lines_in_text(text)
        print(f"Line count: {line_count}; File: {args.file or 'Standard Input'}")

    if args.words:
        word_count = count_words_in_text(text)
        print(f"Word count: {word_count}; File: {args.file or 'Standard Input'}")

    if args.characters:
        character_count = count_characters_in_text(text)
        print(
            f"Character count: {character_count}; File: {args.file or 'Standard Input'}"
        )


if __name__ == "__main__":
    main()
