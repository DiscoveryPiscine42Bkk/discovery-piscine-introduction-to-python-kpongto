# ถามผู้ใช้ให้กรอกตัวเลข
number = float(input("Please enter a number: "))

# เช็คว่าตัวเลขเป็นลบ, บวก หรือศูนย์
if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")
