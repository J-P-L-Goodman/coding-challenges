import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Count the number of bytes in a file.")
    parser.add_argument("file", help="File to count in", nargs="?")
