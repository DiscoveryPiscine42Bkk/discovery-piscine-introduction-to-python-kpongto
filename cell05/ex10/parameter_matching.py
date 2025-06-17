#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    answer = input("What was the parameter? ")
    if answer == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()
