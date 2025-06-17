#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("none")
        return

    # ต้องรวม end ด้วย จึงใช้ end + 1
    if start <= end:
        numbers = list(range(start, end + 1))
    else:
        numbers = list(range(start, end - 1, -1))

    print(numbers)

if __name__ == "__main__":
    main()
