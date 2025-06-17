#!/usr/bin/env python3
import sys

# เมธอดสำหรับย่อสตริงให้เหลือ 8 ตัวแรก
def shrink(text):
    print(text[:8])

# เมธอดสำหรับเติม 'Z' ให้ครบ 8 ตัว
def enlarge(text):
    print(text + 'Z' * (8 - len(text)))

def main():
    if len(sys.argv) < 2:
        print("none")
        return

    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import sys

# เมธอดสำหรับย่อสตริงให้เหลือ 8 ตัวแรก
def shrink(text):
    print(text[:8])

# เมธอดสำหรับเติม 'Z' ให้ครบ 8 ตัว
def enlarge(text):
    print(text + 'Z' * (8 - len(text)))

def main():
    if len(sys.argv) < 2:
        print("none")
        return

    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)

if __name__ == "__main__":
    main()

