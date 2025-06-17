#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("none")
    else:
        print(f"parameters: {len(args)}")
        for param in args:
            print(f"{param}: {len(param)}")

if __name__ == "__main__":
    main()
