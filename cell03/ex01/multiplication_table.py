
def main():
    # รับค่าตัวเลขจากผู้ใช้
    number = int(input("Enter a number: "))
    
    # แสดงตารางการคูณจาก 1 ถึง 10
    for i in range(1, 11):
        print(f"{i} x {number} = {i * number}")

if __name__ == "__main__":
    main()
