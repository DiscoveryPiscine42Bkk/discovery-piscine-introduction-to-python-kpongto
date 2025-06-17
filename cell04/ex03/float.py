number = input("Give me a number: ")

# พยายามแปลงเป็น float และตรวจสอบว่าเป็นจำนวนทศนิยมหรือไม่
try:
    num = float(number)
    # ตรวจสอบว่าเป็นจำนวนทศนิยมจริง ๆ หรือไม่
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("This is not a valid number.")
