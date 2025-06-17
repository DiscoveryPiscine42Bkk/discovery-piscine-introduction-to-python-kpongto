#!/usr/bin/env python3

def main():
    # รับข้อความจากผู้ใช้
    user_input = input()
    
    # สลับพิมพ์เล็ก ↔ พิมพ์ใหญ่ ด้วย .swapcase()
    print(user_input.swapcase())

if __name__ == "__main__":
    main()
