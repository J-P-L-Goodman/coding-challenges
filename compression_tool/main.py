import argparse
import sys


def number_of_occurances(text):
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def main():
    parser = argparse.ArgumentParser(description="Count the number of bytes in a file.")
    parser.add_argument("file", help="File to count in", nargs="?")

    args = parser.parse_args()

    if args.file is None:
        print("Invalid: File not valid")
    else:
        with open(args.file, "rb") as file:
            text = file.read().decode("utf-8")

    char_counts = number_of_occurances(text)
    print(f"{char_counts.get('X')} occurances of X")
    print(f"{char_counts.get('t')} occurances of t")


if __name__ == "__main__":
    main()
