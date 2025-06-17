#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
        return
    
    for param in args:
        # เช็คว่าจบด้วย 'ism' หรือไม่ (case sensitive)
        if not param.endswith("ism"):
            print(param + "ism")

if __name__ == "__main__":
    main()
