# ขอให้ผู้ใช้ป้อนตัวเลขสองตัว
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# คำนวณผลการคูณ
result = num1 * num2

# แสดงผลการคูณ
print(f"{num1} x {num2} = {result}")

# ตรวจสอบผลลัพธ์
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")
